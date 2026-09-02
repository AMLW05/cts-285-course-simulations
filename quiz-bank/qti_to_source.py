#!/usr/bin/env python3
"""Reverse build_qti.py: Canvas QTI 1.2 -> the Markdown question source format.

Reads an unpacked Canvas export and writes one *-source.md per quiz, in the
exact format build_qti.py parses. Round-trips existing Canvas quizzes back into
editable source so they can be revised in the repo and rebuilt.

Usage:
    python3 qti_to_source.py <unpacked_export_dir> --out <dir> [--match SUBSTR]

Example:
    python3 qti_to_source.py _canvas_output/export-26aug --out m2/ --match "Exit Ticket"
"""

from __future__ import annotations

import argparse
import html
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path


def ln(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def find(el, name):
    for c in el.iter():
        if ln(c.tag) == name:
            return c
    return None


def text_of(el) -> str:
    """Flatten an mattext/HTML blob to plain text."""
    if el is None:
        return ""
    raw = "".join(el.itertext())
    raw = html.unescape(raw)
    raw = re.sub(r"<br\s*/?>", " ", raw, flags=re.I)
    raw = re.sub(r"</(p|div|li)>", " ", raw, flags=re.I)
    raw = re.sub(r"<[^>]+>", "", raw)
    raw = html.unescape(raw)
    raw = unicodedata.normalize("NFKC", raw)
    return " ".join(raw.split())


def slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", html.unescape(s))
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[\s_]+", "-", s) or "quiz"


def parse_meta(meta_path: Path) -> dict:
    if not meta_path.exists():
        return {}
    root = ET.parse(meta_path).getroot()
    out = {}
    for name in ("title", "description", "points_possible",
                 "allowed_attempts", "shuffle_answers", "quiz_type"):
        el = find(root, name)
        if el is not None:
            out[name] = text_of(el) if name == "description" else (el.text or "").strip()
    return out


def parse_items(qti_path: Path) -> list[dict]:
    root = ET.parse(qti_path).getroot()
    items = []

    for item in [e for e in root.iter() if ln(e.tag) == "item"]:
        qtype = ""
        for f in item.iter():
            if ln(f.tag) == "fieldlabel" and (f.text or "").strip() == "question_type":
                sib = list(f.getparent()) if hasattr(f, "getparent") else []
                break
        # question_type lives in qtimetadatafield pairs
        for pair in item.iter():
            if ln(pair.tag) == "qtimetadatafield":
                kids = list(pair)
                if len(kids) >= 2 and (kids[0].text or "").strip() == "question_type":
                    qtype = (kids[1].text or "").strip()

        pres = find(item, "presentation")
        if pres is None:
            continue
        stem_el = find(pres, "mattext")
        stem = text_of(stem_el)

        # options
        labels = {}
        for lab in [e for e in pres.iter() if ln(e.tag) == "response_label"]:
            ident = lab.get("ident", "")
            labels[ident] = text_of(find(lab, "mattext"))

        # correct answers
        correct = set()
        for cond in [e for e in item.iter() if ln(e.tag) == "respcondition"]:
            setvar = find(cond, "setvar")
            if setvar is None:
                continue
            try:
                val = float((setvar.text or "0").strip())
            except ValueError:
                val = 0.0
            if val <= 0:
                continue
            for ve in cond.iter():
                if ln(ve.tag) == "varequal" and (ve.text or "").strip():
                    correct.add((ve.text or "").strip())

        # per-option feedback: itemfeedback ident often == "<ident>_fb"
        feedback = {}
        for fb in [e for e in item.iter() if ln(e.tag) == "itemfeedback"]:
            fid = fb.get("ident", "")
            feedback[fid] = text_of(find(fb, "mattext"))

        opts = []
        for ident, otext in labels.items():
            fb = feedback.get(f"{ident}_fb") or feedback.get(ident) or ""
            opts.append({"text": otext, "correct": ident in correct, "fb": fb})

        if stem and opts:
            items.append({"stem": stem, "opts": opts, "type": qtype})

    return items


def emit(quiz_id: str, meta: dict, items: list[dict]) -> str:
    title = html.unescape(meta.get("title", quiz_id))
    out = [f"## QUIZ: {quiz_id} | {title}", ""]

    att = meta.get("allowed_attempts", "").strip()
    shuf = meta.get("shuffle_answers", "").strip()
    pts = meta.get("points_possible", "").strip()
    if att:
        out.append(f"@attempts: {att}")
    if shuf:
        out.append(f"@shuffle: {shuf}")
    if pts and items:
        try:
            out.append(f"@points: {float(pts) / len(items):.1f}")
        except ValueError:
            pass
    if len(out) > 2:
        out.append("")

    desc = meta.get("description", "").strip()
    if desc:
        out.append(f"> {desc}")
        out.append("")

    for n, it in enumerate(items, 1):
        out.append(f"### Q{n}. {it['stem']}")
        out.append("")
        if it["type"] == "multiple_answers_question":
            out.append("TYPE: multiple_answers")
        for o in it["opts"]:
            mark = "x" if o["correct"] else " "
            out.append(f"- [{mark}] {o['text']}")
            if o["fb"]:
                out.append(f"  - FB: {o['fb']}")
        out.append("")

    return "\n".join(out).rstrip() + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("export", type=Path, help="unpacked export directory")
    ap.add_argument("--out", type=Path, default=Path("."), help="output directory")
    ap.add_argument("--match", default="", help="only quizzes whose title contains this")
    ap.add_argument("--combined", default="", help="write all quizzes into one file")
    args = ap.parse_args(argv)

    raw = args.export / "raw"
    if not raw.is_dir():
        print(f"no raw/ under {args.export}", file=sys.stderr)
        return 1

    args.out.mkdir(parents=True, exist_ok=True)
    blocks, report = [], []

    for d in sorted(raw.iterdir()):
        meta_p = d / "assessment_meta.xml"
        if not meta_p.exists():
            continue
        meta = parse_meta(meta_p)
        title = html.unescape(meta.get("title", ""))
        if args.match and args.match.lower() not in title.lower():
            continue

        # The real items live in raw/non_cc_assessments/<id>.xml.qti.
        # The per-quiz assessment_qti.xml is a Common Cartridge stub.
        qti = raw / "non_cc_assessments" / f"{d.name}.xml.qti"
        if not qti.exists():
            qti = next((p for p in d.glob("*.xml") if p.name != "assessment_meta.xml"), None)
        if qti is None or not qti.exists():
            report.append((title, 0, "no qti file"))
            continue

        try:
            items = parse_items(qti)
        except ET.ParseError as e:
            report.append((title, 0, f"parse error: {e}"))
            continue

        if not items:
            report.append((title, 0, "no items recovered"))
            continue

        qid = slug(title)
        blocks.append(emit(qid, meta, items))
        report.append((title, len(items), meta.get("points_possible", "?")))

        if not args.combined:
            (args.out / f"{qid}-source.md").write_text(blocks[-1], encoding="utf-8")

    if args.combined and blocks:
        header = (
            "# Recovered Canvas quiz source\n\n"
            "Generated by qti_to_source.py. Edit here, then rebuild with build_qti.py.\n\n"
            "---\n\n"
        )
        (args.out / args.combined).write_text(header + "\n\n".join(blocks), encoding="utf-8")

    w = max((len(t) for t, _, _ in report), default=10)
    for t, n, p in report:
        print(f"{t[:70]:<{min(w,70)}} | {n:>3} items | pts {p}")
    print(f"\n{len(blocks)} quizzes written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
