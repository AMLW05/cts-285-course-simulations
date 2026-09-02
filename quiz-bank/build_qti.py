#!/usr/bin/env python3
"""Build Canvas Classic Quizzes QTI 1.2 packages from a Markdown question source.

Usage:
    python3 build_qti.py [source.md ...] [--out DIR] [--images images.json]

Defaults: every *-source.md in the current directory, out = ./qti

FORMAT
------
    ## QUIZ: <id> | <title>        start a quiz; <id> names the zip
    @attempts: 3                   allowed attempts (-1 = unlimited)
    @shuffle: true                 shuffle answers
    @points: 1.0                   points per item
    > description text             quiz description (repeatable)

    ### Q1. <stem text>            start an item
    + <raw html>                   appended to the stem verbatim (repeatable)
    TYPE: multiple_answers         optional; default is multiple_choice

    - [x] correct option
      - FB: feedback for that option
    - [ ] distractor
      - FB: feedback for that option
      - IMG: file.png | alt text   optional figure appended to that feedback

Images resolve through images.json ({"file.png": "https://.../preview"}).
An unmapped image is omitted rather than emitted broken, so feedback text must
stand on its own. Never put an IMG in a stem — a missing file would break the
question.
"""

import html
import json
import os
import re
import sys
import zipfile
from xml.sax.saxutils import escape

DEFAULTS = {"attempts": "-1", "shuffle": "true", "points": "1.0"}


# ---------------------------------------------------------------- parsing


def parse(md_text):
    quizzes, quiz, item = [], None, None

    for raw in md_text.splitlines():
        line = raw.rstrip()

        m = re.match(r"^##\s+QUIZ:\s*(\S+)\s*\|\s*(.+)$", line)
        if m:
            quiz = {"id": m.group(1), "title": m.group(2).strip(),
                    "desc": "", "items": [], **DEFAULTS}
            quizzes.append(quiz)
            item = None
            continue

        if quiz is None:
            continue

        m = re.match(r"^@(\w+):\s*(.+)$", line)
        if m and m.group(1) in DEFAULTS:
            quiz[m.group(1)] = m.group(2).strip()
            continue

        m = re.match(r"^>\s?(.*)$", line)
        if m and not quiz["items"]:
            quiz["desc"] = (quiz["desc"] + " " + m.group(1)).strip()
            continue

        m = re.match(r"^###\s+Q(\d+)\.\s+(.+)$", line)
        if m:
            item = {"num": int(m.group(1)), "stem": m.group(2).strip(),
                    "html": [], "type": "multiple_choice_question",
                    "options": []}
            quiz["items"].append(item)
            continue

        if item is None:
            continue

        m = re.match(r"^\+\s(.+)$", line)
        if m:
            item["html"].append(m.group(1))
            continue

        m = re.match(r"^TYPE:\s*(\S+)$", line)
        if m:
            item["type"] = ("multiple_answers_question"
                            if m.group(1).startswith("multiple_answers")
                            else "multiple_choice_question")
            continue

        m = re.match(r"^-\s+\[([xX ])\]\s+(.+)$", line)
        if m:
            item["options"].append({"correct": m.group(1).lower() == "x",
                                    "text": m.group(2).strip(),
                                    "fb": "", "img": None})
            continue

        m = re.match(r"^\s+-\s+FB:\s+(.+)$", line)
        if m and item["options"]:
            item["options"][-1]["fb"] = m.group(1).strip()
            continue

        m = re.match(r"^\s+-\s+IMG:\s+([^|]+)\|\s*(.+)$", line)
        if m and item["options"]:
            item["options"][-1]["img"] = (m.group(1).strip(), m.group(2).strip())
            continue

    return quizzes


def validate(quizzes):
    problems = []
    for q in quizzes:
        if not q["items"]:
            problems.append(f"{q['id']}: no items parsed")
        nums = [i["num"] for i in q["items"]]
        if len(set(nums)) != len(nums):
            problems.append(f"{q['id']}: duplicate question numbers {nums}")
        for it in q["items"]:
            tag = f"{q['id']} Q{it['num']}"
            n_correct = sum(1 for o in it["options"] if o["correct"])
            if len(it["options"]) < 2:
                problems.append(f"{tag}: fewer than 2 options")
            if it["type"] == "multiple_choice_question" and n_correct != 1:
                problems.append(f"{tag}: {n_correct} correct (need exactly 1)")
            if it["type"] == "multiple_answers_question" and n_correct < 2:
                problems.append(f"{tag}: multiple_answers with {n_correct} correct")
            for o in it["options"]:
                if not o["fb"]:
                    problems.append(f"{tag}: no FB for -> {o['text'][:40]}")
    return problems


# ---------------------------------------------------------------- emitting


def para(text):
    return "<p>" + html.escape(text, quote=False) + "</p>"


def fb_html(opt, images):
    out = para(opt["fb"])
    if opt["img"]:
        name, alt = opt["img"]
        url = images.get(name)
        if url:
            out += (f'<p><img src="{html.escape(url, quote=True)}" '
                    f'alt="{html.escape(alt, quote=True)}" '
                    f'style="max-width:460px;height:auto;"></p>')
    return out


def item_xml(quiz, it, images):
    ident = f"{quiz['id']}_q{it['num']}"
    for i, o in enumerate(it["options"]):
        o["ident"] = str(1000 + i)
    multi = it["type"] == "multiple_answers_question"
    card = "Multiple" if multi else "Single"

    stem = para(it["stem"]) + "".join(it["html"])

    labels = "\n".join(
        f'          <response_label ident="{o["ident"]}">\n'
        f'            <material>\n'
        f'              <mattext texttype="text/html">{escape(para(o["text"]))}</mattext>\n'
        f'            </material>\n'
        f'          </response_label>'
        for o in it["options"])

    fb_conds = "\n".join(
        f'      <respcondition continue="Yes">\n'
        f'        <conditionvar>\n'
        f'          <varequal respident="response1">{o["ident"]}</varequal>\n'
        f'        </conditionvar>\n'
        f'        <displayfeedback feedbacktype="Response" linkrefid="{o["ident"]}_fb"/>\n'
        f'      </respcondition>'
        for o in it["options"])

    if multi:
        terms = "\n".join(
            (f'            <varequal respident="response1">{o["ident"]}</varequal>'
             if o["correct"] else
             f'            <not><varequal respident="response1">{o["ident"]}</varequal></not>')
            for o in it["options"])
        score_cond = (f'      <respcondition continue="No">\n'
                      f'        <conditionvar>\n'
                      f'          <and>\n{terms}\n          </and>\n'
                      f'        </conditionvar>\n'
                      f'        <setvar action="Set" varname="SCORE">100</setvar>\n'
                      f'      </respcondition>')
    else:
        correct = next(o for o in it["options"] if o["correct"])
        score_cond = (f'      <respcondition continue="No">\n'
                      f'        <conditionvar>\n'
                      f'          <varequal respident="response1">{correct["ident"]}</varequal>\n'
                      f'        </conditionvar>\n'
                      f'        <setvar action="Set" varname="SCORE">100</setvar>\n'
                      f'      </respcondition>')

    feedback = "\n".join(
        f'    <itemfeedback ident="{o["ident"]}_fb">\n'
        f'      <flow_mat>\n'
        f'        <material>\n'
        f'          <mattext texttype="text/html">{escape(fb_html(o, images))}</mattext>\n'
        f'        </material>\n'
        f'      </flow_mat>\n'
        f'    </itemfeedback>'
        for o in it["options"])

    return f"""    <item ident="{ident}" title="Question {it['num']}">
      <itemmetadata>
        <qtimetadata>
          <qtimetadatafield>
            <fieldlabel>question_type</fieldlabel>
            <fieldentry>{it['type']}</fieldentry>
          </qtimetadatafield>
          <qtimetadatafield>
            <fieldlabel>points_possible</fieldlabel>
            <fieldentry>{quiz['points']}</fieldentry>
          </qtimetadatafield>
          <qtimetadatafield>
            <fieldlabel>assessment_question_identifierref</fieldlabel>
            <fieldentry>{ident}_aq</fieldentry>
          </qtimetadatafield>
        </qtimetadata>
      </itemmetadata>
      <presentation>
        <material>
          <mattext texttype="text/html">{escape(stem)}</mattext>
        </material>
        <response_lid ident="response1" rcardinality="{card}">
          <render_choice>
{labels}
          </render_choice>
        </response_lid>
      </presentation>
      <resprocessing>
        <outcomes>
          <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
        </outcomes>
{fb_conds}
{score_cond}
      </resprocessing>
{feedback}
    </item>"""


def assessment_xml(quiz, images):
    items = "\n".join(item_xml(quiz, it, images) for it in quiz["items"])
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">
  <assessment ident="{quiz['id']}" title="{escape(quiz['title'])}">
    <qtimetadata>
      <qtimetadatafield>
        <fieldlabel>cc_maxattempts</fieldlabel>
        <fieldentry>{'unlimited' if quiz['attempts'] == '-1' else quiz['attempts']}</fieldentry>
      </qtimetadatafield>
    </qtimetadata>
    <section ident="root_section">
{items}
    </section>
  </assessment>
</questestinterop>
"""


def meta_xml(quiz):
    points = len(quiz["items"]) * float(quiz["points"])
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<quiz identifier="{quiz['id']}" xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <title>{escape(quiz['title'])}</title>
  <description>{escape(para(quiz['desc']))}</description>
  <shuffle_answers>{quiz['shuffle']}</shuffle_answers>
  <scoring_policy>keep_highest</scoring_policy>
  <hide_results></hide_results>
  <quiz_type>assignment</quiz_type>
  <points_possible>{points}</points_possible>
  <require_lockdown_browser>false</require_lockdown_browser>
  <require_lockdown_browser_for_results>false</require_lockdown_browser_for_results>
  <require_lockdown_browser_monitor>false</require_lockdown_browser_monitor>
  <allowed_attempts>{quiz['attempts']}</allowed_attempts>
  <one_question_at_a_time>false</one_question_at_a_time>
  <cant_go_back>false</cant_go_back>
  <available>true</available>
  <one_time_results>false</one_time_results>
  <show_correct_answers>true</show_correct_answers>
  <show_correct_answers_last_attempt>false</show_correct_answers_last_attempt>
  <anonymous_submissions>false</anonymous_submissions>
  <could_be_locked>false</could_be_locked>
  <disable_timer_autosubmission>false</disable_timer_autosubmission>
  <assignment_group_identifierref>quizzes_group</assignment_group_identifierref>
  <only_visible_to_overrides>false</only_visible_to_overrides>
  <module_locked>false</module_locked>
</quiz>
"""


def manifest_xml(quiz):
    qid = quiz["id"]
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{qid}_manifest" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p2_v1p0.xsd">
  <metadata>
    <schema>IMS Content</schema>
    <schemaversion>1.1.3</schemaversion>
  </metadata>
  <organizations/>
  <resources>
    <resource identifier="{qid}" type="imsqti_xmlv1p2">
      <file href="{qid}/{qid}.xml"/>
      <dependency identifierref="{qid}_dep"/>
    </resource>
    <resource identifier="{qid}_dep" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="{qid}/assessment_meta.xml">
      <file href="{qid}/assessment_meta.xml"/>
    </resource>
  </resources>
</manifest>
"""


# ---------------------------------------------------------------- main


def main():
    args = sys.argv[1:]
    outdir, imgfile, srcs = "qti", "images.json", []
    i = 0
    while i < len(args):
        if args[i] == "--out":
            outdir = args[i + 1]; i += 2
        elif args[i] == "--images":
            imgfile = args[i + 1]; i += 2
        else:
            srcs.append(args[i]); i += 1

    if not srcs:
        srcs = sorted(f for f in os.listdir(".") if f.endswith("-source.md"))
    if not srcs:
        print("no source files found"); sys.exit(1)

    images = {}
    if os.path.exists(imgfile):
        with open(imgfile, encoding="utf-8") as fh:
            images = {k: v for k, v in json.load(fh).items() if v}

    quizzes = []
    for s in srcs:
        with open(s, encoding="utf-8") as fh:
            quizzes.extend(parse(fh.read()))

    problems = validate(quizzes)
    if problems:
        for p in problems:
            print("ERROR:", p)
        sys.exit(1)

    os.makedirs(outdir, exist_ok=True)
    for q in quizzes:
        path = os.path.join(outdir, q["id"] + ".zip")
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("imsmanifest.xml", manifest_xml(q))
            z.writestr(f"{q['id']}/{q['id']}.xml", assessment_xml(q, images))
            z.writestr(f"{q['id']}/assessment_meta.xml", meta_xml(q))
        att = "unlimited" if q["attempts"] == "-1" else q["attempts"]
        print(f"OK  {path}  ({len(q['items'])} items, {att} attempts)")

    missing = sorted({o["img"][0] for q in quizzes for it in q["items"]
                      for o in it["options"] if o["img"]} - set(images))
    for m in missing:
        print(f"NOTE: image not mapped in {imgfile}, omitted from feedback: {m}")


if __name__ == "__main__":
    main()
