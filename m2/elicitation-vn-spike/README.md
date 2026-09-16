# M2 Elicitation — visual-novel design spike

> **NOT STUDENT MATERIAL. NOT LINKED FROM CANVAS. NOT IN ANY MODULE SEQUENCE.**
>
> This directory sits beside `m2/stakeholder-elicitation/` and `m2/arcade/`, which *are* student
> material launched from Canvas. **This one is not.** It is a design spike, and the word is in the
> directory name so it stays visible in every path, every URL, and every link anyone is tempted
> to paste.

A spike exists to answer a design question by building the smallest real thing that answers it.
**A spike graduates by being rebuilt under its own build guide, or it is deleted. It never
graduates by being linked to.**

| Question it exists to answer | State |
|---|---|
| Can the Module 2 elicitation rebuild carry a visual-novel form — branching dialogue, world-state gauges, consequence instead of score — without becoming a hidden-perfect-path quiz? | open |

## What it is

One scene, two routes, built to be driven from the front of a room in about ten minutes.

**A linear prologue, then the interview.** The prologue is eleven beats with no choices and no
cost. It runs on the interview's own stage rather than a screen of its own, so the three
silhouettes, the dialogue line and the two gauges are learned in the place they will be used
instead of arriving cold at the first decision. The gauges appear when they are explained; the
question budget appears when it is granted.

The prologue delivers **the shipped simulation's four opening stakeholder statements, verbatim**,
as spoken lines — *"Make DataMan modern," "Keep it simple," "Students shouldn't lose their work,"
"Parents should still understand what the child is doing."* It closes on the observation those
four invite: not one of them can be tested, and **the learner has not been asked anything at
all.**

Then the interview. The seven prompt strings are **copied exactly** from
`../stakeholder-elicitation/index.html`, so the scene reads continuous with what students already
did rather than as a toy. The spoken replies are written for this scene — the shipped file
carries evidence text but no dialogue.

Route A spends the budget on questions that establish no need; Route B on questions that do.
**Both cost exactly two questions.** The complication then arrives for both. A standalone
comparison screen puts the two side by side and is the projector payload.

**Bypasses, for a second run in front of a room:** *Skip to the questions* and *Skip to the
comparison* on the briefing screen. Re-running a route never replays the prologue.

## Constraints it is built under, which any rebuild inherits

- **The gauges describe the project, not the student.** *Project complexity* and *schedule
  pressure* are world state. A gauge a student reads as a score is a badge whatever it is called,
  and the 2026-09-02 formative mechanics decision forbids it.
- **Endings are not ranked.** Route labels are *spend on solutions* and *spend on needs*, never
  *wrong* and *right*. Four terminal positions, each with a different cost, none scored.
- **No FTCC gold anywhere.** The confirmed institutional gold `#F0B82D` sits 13 from PRISM yellow
  `#F2C037` out of 441 — closer than the retired `#E3B23C` estimate's 21 — and
  `INTERSTITIAL-MODULES.md` rule 4 forbids institutional colour where a band claim would be read.
  This file is in-character throughout, so it carries band colour and no institutional colour at
  all. It also satisfies the root README's rule that student-facing external experiences carry no
  institutional branding, though it is not student-facing.
- **Never colour alone.** Every gauge movement is worded as well as drawn.
- Keyboard operable throughout; silhouettes carry `aria-label`; beats and gauge changes announce
  through a live region; `prefers-reduced-motion` respected.

## Known simplifications, which are the spike's findings

- **Three prompts surface at a time against a two-question budget**, so one run reaches only part
  of the bank. The shipped simulation shows all seven at once and allows three. A rebuild has to
  decide whether progressive disclosure is a feature — it is what makes an interview feel like a
  conversation — or an accidental narrowing of the choice the constraint exists to teach.
- **The prologue is linear on purpose.** Whether the rebuild can afford eleven beats before the
  first decision is a pacing question the spike exists to let people argue about in front of a
  room rather than in prose.

## Unresolved, and the reason the spike exists

Putting the Channel Success Partner on the elicitation simulation would be **the first time the
AlgoCratic fiction touches assessed work** — the shipped simulation feeds
`docs/decisions/m2-elicitation-decision-record.md` and, through it, the graded Requirements
Register.

The 2026-09-16 decision in `cts-285_SOURCE` permits kayfabe in standalone and Canvas material
**only with express approval, item by item, and grants no approval.** Nothing about this file
existing changes that. The decision is taken in `cts-285_SOURCE`, not here.
