# CTS-285 Course Simulations

Public student-facing interactive material for CTS-285 Systems Analysis & Design.

Course instructions, alignment, assessment directions, rubrics, and grading live in Canvas and in the private CTS-285 source-of-truth repository. This repository holds the external interactive experiences students open and run, plus support copies/templates used to keep those experiences aligned.

## Module 4 — current sequence

Module 4 is no longer represented by one short form-style simulation. The external sequence is:

1. `m4/practice-cabinet/` — Design Decisions Cabinet
2. `m4/design-investigation/` — Investigation Brief
3. `m4/answer-flow-lab/` — operational two-attempt behavior simulation
4. `m4/memory-bank-lab/` — operational set/data/retrieval simulation
5. `m4/design-studio/` — student-selected Design Studio / synthesis

Use `m4/index.html` as the student-facing sequence hub.

Authoritative external alignment/verification files:
- `m4/M4_ALIGNMENT_AND_SEQUENCE.md`
- `m4/M4-ASSET-MANIFEST.md`

Record templates:
- `m4/templates/m4-investigation-brief-template.md`
- `m4/templates/m4-lab-evidence-record-template.md`
- `m4/templates/m4-design-investigation-record-template.md`

Canvas support copies are retained under `m4/canvas/` so the simulation architecture and Canvas handoffs can be checked together. The authoritative Canvas/module production order remains in `AMLW05/cts-285_SOURCE`.

## Earlier graded simulations

| Simulation | Path | Produces |
|---|---|---|
| Stakeholder Elicitation Under Pressure | `m2/stakeholder-elicitation/` | `docs/decisions/m2-elicitation-decision-record.md` |
| Backlog Triage — What Moves Forward? | `m3/backlog-triage/` | `docs/decisions/m3-backlog-triage-record.md` |
| Product Owner Sprint Simulation | `m3/product-owner-sprint/` | `docs/decisions/m3-product-owner-decision-record.md` |

## M2 embedded case and practice experiences

| Experience | Path | Role |
|---|---|---|
| DataMan Elicitation Case | `m2/dataman-elicitation-case/` | M2.3 Apply/Gauge case; replaces the former multi-page Canvas branch tree and feeds the DataMan Requirements Register |
| Evidence-to-Requirement Lab | `m2/evidence-to-requirement/` | M2.4 controlled practice; keeps translation decisions and quality checks outside Canvas while preserving the source-of-truth content |

The authoritative M2.3 and M2.4 content and alignment remain in `AMLW05/cts-285_SOURCE`. This repository changes only the delivery format so students can work through interactive decisions without fragile Canvas page-to-page routing.

Module 4 uses a cumulative sequence instead of treating the pre-studio Investigation Brief as the graded simulation. The graded Design Investigation evidence is captured later through Canvas using `docs/decisions/m4-design-investigation-record.md`.

## Practice

| Item | Path | Graded |
|---|---|---|
| Story Builder Lab | `m3/story-builder/` | No — nothing submitted separately |
| Field Analyst Arcade — DataMan Case Prep | `m1/arcade/` | No |
| DataMan Field Check — Requirements Survey | `m2/arcade/` | No |
| Evidence-to-Requirement Lab | `m2/evidence-to-requirement/` | No — nothing submitted separately |
| Backlog Bench — Product Work Survey | `m3/arcade/` | No |
| Design Decisions Cabinet | `m4/practice-cabinet/` | No — formative practice |

Practice experiences submit nothing to an external service. They exist to let students test a judgment before applying it to project work.

## Quiz bank

`quiz-bank/` holds question sources and built QTI packages for exit tickets and guided analyses, plus the build script. See `quiz-bank/README.md` for the format contract, build command, and status of each source.

Exit tickets are not practice cabinets. The cabinet drills a skill; the ticket checks whether the skill transfers to a new situation.

## Conventions

- Every student-facing simulation page is self-contained HTML/CSS/JS.
- No login is required.
- No external data storage is used.
- No network calls are required by the M4 experiences.
- Browser state is local only and may be transient unless the activity deliberately uses local browser persistence.
- Consequences are shown rather than scored silently.
- When multiple professional decisions are defensible, the experience should not pretend there is one hidden perfect route.
- Primary drag interactions require an accessible non-drag alternative.
- Student-facing external experiences contain no institutional branding.

## Not student material

`m2/elicitation-vn-spike/` is a **design spike**, deliberately absent from every sequence table
above. It is not linked from Canvas, is not part of any module sequence, and must not be given to
students. It carries its own README stating the same. It is listed here only so that nobody
finding it in `m2/` has to guess what it is.

## Verification status

M4 has an explicit asset manifest and cross-repository sequence map. The remaining production check is live human playtesting of the deployed paths and the Canvas-to-hosted-URL wiring before the module is locked.
