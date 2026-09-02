# CTS-285 Course Simulations

Public student-facing interactive material for CTS-285 Systems Analysis & Design.

Course instructions, alignment, assessment directions, rubrics, and grading live in Canvas and
in the private CTS-285 source-of-truth repository. This repository holds only what a student
actually opens and runs.

## Graded simulations

Each one generates a decision record the student copies into their own GitHub repository. The
Canvas page names the exact path.

| Simulation | Path | Produces |
|---|---|---|
| Stakeholder Elicitation Under Pressure | `m2/stakeholder-elicitation/` | `docs/decisions/m2-elicitation-decision-record.md` |
| Backlog Triage — What Moves Forward? | `m3/backlog-triage/` | `docs/decisions/m3-backlog-triage-record.md` |
| Product Owner Sprint Simulation | `m3/product-owner-sprint/` | `docs/decisions/m3-product-owner-decision-record.md` |

## Practice

| Item | Path | Graded |
|---|---|---|
| Story Builder Lab | `m3/story-builder/` | No — nothing submitted separately |
| Field Analyst Arcade — DataMan Case Prep | `m1/arcade/` | No |
| DataMan Field Check — Requirements Survey | `m2/arcade/` | No |
| Backlog Bench — Product Work Survey | `m3/arcade/` | No |

**The arcades are optional and ungraded.** They submit nothing, record nothing, and are visible
to no one. They exist to let a student find a weak spot before an assignment. Early student
response is that they are a useful way to get familiar with the concepts — which is the whole
job. They are not load-bearing and should not be assessed as though they were.

## Quiz bank

`quiz-bank/` holds the question sources and built QTI packages for exit tickets and guided
analyses, plus the build script. See `quiz-bank/README.md` for the format contract, the build
command, and the current status and known staleness of each source.

Exit tickets are **not** arcades. They share a bank of discriminations but never a specific
item: the arcade drills the skill, the ticket confirms it transferred, and a student who
memorised a cabinet item gains nothing on a ticket.

## Conventions

- Every page is self-contained. No build step, no external dependencies, no network calls.
- State is `localStorage` only. Nothing leaves the browser.
- No simulation has a single hidden correct path. The runtime enforces only genuine scenario
  constraints, such as capacity or a release-critical defect.
- Consequences are shown, not scored silently.

## Verification status

Everything here passes its own checks and **none of it has been click-tested end to end by a
human.** Until it has, any claim about how it behaves for a student is a claim about a design.
Playtesting is tracked in the source-of-truth repository.
