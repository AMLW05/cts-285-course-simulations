# Quiz bank

Question sources and built QTI packages for CTS-285 exit tickets and guided analyses.

**Staged 2026-09-02, pending review.** Nothing here is finished work. It is placed so it stops
living in an untracked scratch folder on one laptop, and so the staleness notes below have
somewhere to be recorded. See the tracking issue for what is and is not settled.

## Layout

```
build_qti.py                     source .md  ->  QTI .zip
qti_to_source.py                 QTI .zip    ->  source .md   (recovery direction)
images.json                      image filename -> Canvas file URL
m1-exit-tickets-source.md        3 quizzes, 15 items
m1-guided-analysis-source.md     2 quizzes, 21 items
m2-exit-tickets-source.md        1 quiz, 5 items
m3-exit-tickets-source.md        1 quiz, 5 items
qti/                             7 built packages
```

## Build

```
python3 build_qti.py m2-exit-tickets-source.md --out qti/
```

The source `.md` is the source of truth. Edit it and rebuild; do not hand-edit a `.zip`.
`qti_to_source.py` runs the other direction and exists for recovering a package whose source
was lost — it is not part of the normal loop.

**Run the build from inside `quiz-bank/`.** `build_qti.py` looks for `images.json` in the
working directory unless you pass `--images`. Building from elsewhere finds no map and silently
drops every image (see below).

## Images

A source line of the form `- IMG: <file.png> | <alt text>` appends an image to that option's
feedback. `images.json` maps the filename to a Canvas Files URL:

```json
{ "dataman-keypad.png": "https://faytechcc.instructure.com/courses/11777/files/8857654/preview" }
```

The PNGs are uploaded to Canvas Files by hand; only the resulting URLs live here. Two images are
mapped today, both in `m1-guided-analysis-source.md`.

**An unmapped image is omitted, not broken.** `build_qti.py` prints a `NOTE:` line and still
reports `OK`. That is the right default — a missing image beats a broken one in a live quiz —
but it means a build can quietly produce a package worse than the one it replaces. If you touch
the guided analyses, read the NOTE lines, not just the OK lines.

## Format contract

`build_qti.py` parses these literally. Breaking one silently produces a wrong package.

- `## QUIZ: <id> | <title>` starts a quiz. `<id>` becomes the zip and folder name.
- `> <text>` directly under a quiz heading becomes the quiz description.
- `### Q<n>. <stem>` starts an item.
- `- [x]` marks the correct option, `- [ ]` a distractor.
- `  - FB: <text>` on the line after an option is that option's feedback.
- Blank lines separate items. No other Markdown inside stems or options.

Every item is multiple choice, one correct answer, and **every option carries feedback** —
including the correct one. A distractor without feedback is a scoring event with nothing taught.

## Why the built `.zip` files are committed

They are build artifacts, which normally would not be tracked. They are here because:

- The M1 packages are **already installed and live in Canvas.** The committed zip is the record
  of what students actually received, which a rebuild from source would not guarantee to
  reproduce byte for byte.
- There is no CI in this repository to rebuild them on demand.

If a source and its zip ever disagree, the source wins for future builds and the zip stands as
the historical record of what shipped.

### Reproducibility check — 2026-09-03

All seven packages were rebuilt from source and the unzipped XML compared against the committed
zip. Five reproduce exactly. `cts285-m1-guided-a` and `cts285-m1-guided-b` differed by one image
each — the rebuild dropped them, because `images.json` had not been committed alongside the
sources. Adding it closes the gap; the committed zips were correct and were not rebuilt.

Reproducing is not the same as being correct. It means a rebuild will not silently downgrade a
package. Whether the questions work on a student is a separate claim, and only the three M1 exit
tickets and two guided analyses have any evidence for it.

## Status of each source

| Source | Canvas state | Notes |
|---|---|---|
| `m1-exit-tickets-source.md` | **Live** | Already installed. Staged for continuity, not for placement. |
| `m1-guided-analysis-source.md` | **Live** | Same. |
| `m2-exit-tickets-source.md` | **Not placed** | Module 2 is locked against added exit tickets. Staging the source is not placing it in Canvas. |
| `m3-exit-tickets-source.md` | **Not placed** | Needs the "instructionally necessary" justification, or withdrawal. Undecided. |

## Known staleness

**`m3-exit-tickets-source.md` — two point values in its justification table are wrong.**

| It says | Actual |
|---|---|
| Backlog Triage Decision Record (10 pts) | **8** |
| Product Owner Decision Record (12) | **10** |

Not corrected here on purpose. That table exists to argue the ticket is necessary, and whether
the ticket ships at all is undecided — fixing the argument for something that may be withdrawn
presumes the outcome. Correct it if and when the ticket is approved.

The rest of that table checks out: the Acceptance Criteria Lab is 10 points, the DataMan Product
Backlog is 20, and the Story Builder Lab does still state that nothing from it is submitted
separately. **The argument survives its stale evidence** — stories remain the one half of
MLO 3.1 with no Canvas-visible check.

**`m2-exit-tickets-source.md` is not stale.** It was written against the 1977 device before
Module 2's elicitation case was repointed to match. Its Q1 — a teacher reporting that learners
got frustrated — now mirrors the shipped M2.3 briefing almost exactly.

## Relationship to the arcades

The arcades in `m1/arcade/`, `m2/arcade/`, and `m3/arcade/` drill the same discriminations these
tickets assess, deliberately using **different instances**. No stem in a ticket appears in a
cabinet. A student who drilled the skill transfers; one who memorised an item does not.

The arcades are optional and ungraded. The tickets are neither. Do not merge the two banks.
