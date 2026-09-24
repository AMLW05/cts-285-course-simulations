# CTS-285 Simulations Project Tracking

**Purpose:** retrospective + current tracking for hosted simulations, arcades, QTI sources, starter distributions, and other student-facing runtimes. Course architecture and grading decisions remain authoritative in `AMLW05/cts-285_SOURCE`.

## Milestone map

| Milestone | Scope | State |
|---|---|---|
| #14 — Analysis practice runtimes | M1–M3 | **Complete** |
| #15 — Design and implementation runtimes | M4–M5 | **Built** |
| #16 — Runtime QA, reproducibility, and current-run cleanup | Cross-repo parity and validation | **Active** |

## How the runtime work evolved

### 1. Analysis practice runtimes — M1–M3

The repository began as hosted practice support and then became the canonical home for runtime assets and script-built quiz packages.

Progression:
- PR #1 added the M2 DataMan Field Check.
- PR #3 staged M1/M3 arcades and the quiz bank so live/working material stopped living only in Canvas or on one machine.
- PR #4 removed a remote font dependency so the M1 arcade remained self-contained.
- PRs #6–#8 reconciled arcade mechanics with course governance: rank/lives/loss framing were removed, while cumulative practice evidence remained.
- PR #9 added the image map so QTI packages rebuild reproducibly.
- PRs #11–#13 evolved the M2 elicitation runtime from a design spike into a placed, indexed student experience.

Result: M1–M3 practice became versioned, self-contained, and explicitly separated from graded Canvas evidence.

### 2. Design and implementation runtimes — M4–M5

The simulation role changed: from analysis judgment to making design and implementation boundaries visible.

M4 runtime set:
- practice cabinet;
- design investigation;
- answer-flow lab;
- memory-bank lab;
- design studio;
- lab evidence record.

M5 runtime set:
- Flask responsibility lab;
- Flask build lab;
- starter distribution.

The governing design principle is the same implementation spine recorded in the private source: interface/framework responsibility, reusable business logic, and data/state responsibility remain distinguishable across the transition from prototype to Flask.

### 3. Runtime QA, reproducibility, and current-run cleanup

Active work under #16 should stay limited to correctness and parity:

- human click-testing of load-bearing experiences;
- QTI/source reproducibility;
- source ↔ distributed starter parity;
- marking/removing withdrawn public Canvas copies;
- fixing identifier drift between labs and the governed starter;
- provenance headers where exported/support copies intentionally differ;
- cross-repo links so a runtime always points back to the course decision/assignment it serves.

Do **not** use this milestone to invent new course scope. M6–M8 may legitimately use the student's own repository rather than hosted simulations.

## Cross-repo ownership

- **CTS-285 source repo:** module architecture, Canvas HTML, rubrics, human New Quiz build guides, alignment, grading/evidence decisions.
- **This repo:** hosted runtimes, runtime assets, script inputs, QTI build/conversion pipeline, built QTI packages, and student support copies/templates needed by those runtimes.
- When the two disagree about course meaning, the private CTS-285 source wins.

## Tracking rules going forward

1. Every runtime PR should name the CTS-285 module/item or source issue it supports.
2. Runtime QA and content/course-design decisions are separate; report design findings back to the source repo rather than silently deciding them here.
3. Keep known withdrawn/superseded copies visibly marked if retained for history.
4. Reproducibility findings belong under #16, even when the original runtime milestone is closed.
5. A hosted experience should remain practice/evidence support, not become a second grading system.
