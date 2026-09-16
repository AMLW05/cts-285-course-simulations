# Spikes

**Nothing in this directory is student material.** Spikes are not linked from any Canvas page,
are not part of any module sequence, and are not listed in the root `README.md` sequence tables.
A spike exists to answer a design question by building the smallest real thing that answers it.

A spike graduates by being rebuilt somewhere else under its own build guide, or it is deleted.
It never graduates by being linked to.

| Spike | Question it exists to answer | State |
|---|---|---|
| `vn-elicitation-scene/` | Can the Module 2 elicitation rebuild carry a visual-novel form — branching dialogue, world-state gauges, consequence instead of score — without becoming a hidden-perfect-path quiz? | open |

## `vn-elicitation-scene/`

One scene, two routes, built to be driven from the front of a room in about ten minutes.

It reuses the shipped simulation's seven questions verbatim so the contrast is continuous with
what students already did, rather than a toy. Route A spends the budget on questions that
establish no need; Route B spends it on questions that do. **Both cost exactly two questions.**
The complication then arrives for both.

**Deliberate constraints it is built under, and which any rebuild inherits:**

- **The gauges describe the project, not the student.** *Project complexity* and *schedule
  pressure* are world state. A gauge a student reads as a score is a badge, whatever it is
  called, and the 2026-09-02 formative mechanics decision forbids it.
- **Endings are not ranked.** They are different terminal positions with different costs. The
  route labels say *spend on solutions* and *spend on needs*, never *wrong* and *right*.
- **No FTCC gold anywhere.** The confirmed institutional gold `#F0B82D` sits 13 from PRISM
  yellow `#F2C037` out of 441 — closer than the retired `#E3B23C` estimate's 21 —
  and `INTERSTITIAL-MODULES.md` rule 4 forbids placing institutional colour where a band claim
  would be read. This file is in-character throughout, so it carries band colour and no
  institutional colour at all.
- **Never colour alone.** Every gauge movement is worded as well as drawn.
- Keyboard operable throughout; silhouettes carry `aria-label`; gauge changes announce through a
  live region.

**Unresolved, and the reason the spike exists:** putting the Channel Success Partner on the
elicitation simulation is the first time the AlgoCratic fiction touches assessed work.
`INTERSTITIAL-MODULES.md` currently confines the character to interstitials and arcades. That is
a decision to be taken deliberately in `cts-285_SOURCE`, not settled by this file existing.
