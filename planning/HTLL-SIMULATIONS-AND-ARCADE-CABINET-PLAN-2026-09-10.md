# High Tech Low Lives simulations and the arcade cabinet — plan, 2026-09-10

**Status: proposed. Nothing here is decided and nothing here is built.** This is a plan for
three parallel work products. It records what each one is, which rules bind it, what it borrows
from the two repositories, and what the course owner has to decide before any of it is placed in front of
a student. Later dated decisions in the private source repository's `planning/DECISIONS.md`
supersede anything here.

This file lives in the public simulations repository by the course owner's direction of 2026-09-10: the
simulation material for CTS-285 belongs where the simulations run. Every `planning/…`,
`module-XX/…`, `binder/…`, and `.claude/…` path cited below is a path in the private
`AMLW05/cts-285_SOURCE` repository unless it says otherwise.

HTLL means *High Tech Low Lives*, the Fate-based cyberpunk RPG in
`norrisaftcc/game-high-tech-low-lives`. Its companion file on that side is `arcade/README.md`
in that repository. The two files do not repeat each other: this one holds the pedagogy and the
governance; that one holds the persona rules, the cartridge format, and the reference build.

---

## 1 · The brief, written to the floor

Three products, built in parallel, each demonstrable on its own:

| Product | What it is | Governed by |
|---|---|---|
| **A · HTLL transfer simulations** | Decision simulations in the HTLL world that keep every CTS-285 pedagogical element: the pattern, the constraint, the decision record, the project update | CTS-285 rules in full |
| **B · The arcade cabinet** | One in-character HTML mini-game per CTS-285 module, in the register of *Hard/Wired Coast*. The player picks two personas from the HTLL playbooks. CTS-285 principles are the code's underlying structure, not its surface | HTLL rules, plus a CTS-285 *classroom profile* if one is ever launched from Canvas |
| **0 · The cabinet shell** | The shared runtime both A and B run in, hardened from the *Hard/Wired Coast* reference build and its review | Neither; internal tooling |

Ground truth for each side:

- **CTS-285** supplies the pedagogy: STAGE, the chain *Evidence → Need → Requirement → User
  Story → Acceptance Criteria → Backlog Decision → Priority*, the simulation pattern *Brief →
  Constraint → Choice → Consequence → Decision Record → Project Update*, and the decision-record
  format the students already write.
- **HTLL** supplies the world (pelagic, corporate, 93 % ocean), the tone, the four playbooks
  (Infiltrator, Influencer, Nomad, Fixer), the 4dF resolution ladder, and two early attempts at
  simulated play: the Python narrative engine in `prototype/` and the Twine scene in
  `build/shodann-solo/`.
- **Aesthetic references**: the 1977 TI DataMan and *The Story of DataMan* booklet; Windows 95
  dialogs and the Office Assistant; *Hard/Wired Coast* (CRT shmup, event banter);
  *White Knuckle* (vertical industrial ascent, rising threat, low-poly dread); *Trepang2*
  (corporate blacksite, slow-motion breach); *Suspended* (Infocom, 1983: a frozen human directs
  six robots, each with one sense, while a planet's systems fail).

The single most useful discovery in the research: **the two fictions are already one world.**
HTLL's antagonist corporation is *AlgoCratic-Fujikara* and its front is *The Algorithm*, an
emergent AI. CTS-285's kayfabe is *AlgoCratic Futures*, *SHODANN*, *the Creators*, and the PRISM
bands. Product B does not have to invent a crossover; it has to reconcile two spellings of the
same one (see §9).

---

## 2 · Which rules bind which product

| Rule (source) | A · Simulations | B · Arcade | 0 · Shell |
|---|---|---|---|
| Pattern Brief → Constraint → Choice → Consequence → Decision Record → Project Update (`SIMULATION-ARCHITECTURE-M2-M4.md:9`) | binds | binds, as the level structure | supports |
| No disguised multiple-choice quiz; no single hidden perfect path; consequences exposed (`:11`, `:90`) | binds | binds | — |
| Copyable Markdown evidence at the end (`:15-24`) | binds | binds | provides |
| Runtime lives in the public `AMLW05/cts-285-course-simulations`; this repository holds spec and launch page only (`REPOSITORY-OWNERSHIP.md`) | binds | binds only if Canvas launches it | internal |
| Fiction never on an instructional page; in-character material lives in an unnumbered interstitial with a signposted entry and a visible exit (`SKILL.md:152-190`) | binds | binds if Canvas launches it | provides the exit bar |
| No asynchronous in-character module ships without the async distress button (`KAYFABE-MEETING-2026-09-03.md`, item 8) | binds | binds if Canvas launches it | provides F1 / F2 / Canvas link |
| Formative mechanics: no XP, points-as-currency, badges, leaderboards, hearts, lives, timers, streaks (`DECISIONS.md:181-190`) | binds | **binds only under the classroom profile** (§5.4) | profile switch |
| Two-product rule: DataMan is the device and the project; ADS is the corporate transfer scenario; never DataMan-as-a-company (`DECISIONS.md:45-52`) | binds (§9, decision 2) | binds where a client is named | — |
| Do not invent DataMan behaviours (`CLAUDE.md`) | binds | binds | — |
| M2 is locked; the M2 elicitation simulation is not redesigned (`BUILD-STATUS.md`) | binds: A adds beside, never replaces | binds | — |
| M5–M8 are spine planning only; do not expand (`BUILD-STATUS.md:20`) | binds | binds: M5–M8 cartridges are one-line sketches | — |
| HTLL Phase 3 (technical implementation) is deferred; React vetoed (HTLL `CLAUDE.md`) | — | binds: single-file HTML, no framework | binds |

The consequence of the table: **Product B is an HTLL product by default.** It borrows CTS-285's
structure for its code. It becomes CTS-285 material only when the course owner places a cartridge in an
interstitial, and at that moment the classroom profile applies. The profile does not strip the
stakes. It converts them: hull becomes capacity, score becomes recorded shifts, the clock
becomes a complication. The course teaches prioritisation and trade-offs, so stakes handled in
character are course material, not a breach of it. The cabinet is designed so the conversion is
one flag, not a rebuild. Where a stake will not convert, the cartridge ships under the
*demonstration* label instead (§5.4).

---

## 3 · Product 0 — the cabinet shell

*Hard/Wired Coast* (field build 0.8, one file, touch only) is the reference build. The review
of 2026-09-10 read its control logic, pacing values, and dialogue triggers, because no human
playtest notes existed and the browser runner would not launch. The review's findings become
the shell's first sprint, unchanged:

| Priority | Change | Reason |
|---|---|---|
| Must | Remove TRACE's "left 43 % means steering" rule | It blocks direct shots at enemies on the left |
| Must | Add an aim reticle and lock confirmation | TRACE gives little feedback on shot direction |
| Must | Dead zone and normalised movement in DUAL VECTOR | Centre press makes stationary shots; diagonals are faster than straight |
| Must | Reduce the Overlord from 198 required hits to about 90–100 | At realistic touch accuracy the boss outlasts both shore stages |
| Must | Replace timed banter with event-driven banter | Ten-second remarks feel detached; low-hull remarks overwrite each other |
| Should | One-second stage-clear beat | Threats vanish and the stage changes in the same frame |
| Should | Keep pads clear of the air car in portrait | The dual pads overlap the main action area |
| Should | Let the final Overlord line finish | The results overlay hides most of the four-second defeat line |
| Later | Optional short haptics | Fire, damage, relay loss, shield failure |

Recommended pacing stays as reviewed: Black Tide 15–20 s, Hard Land 15–20 s, Overlord 20–30 s,
a full sortie about one minute.

What the shell adds beyond the review, because every cartridge needs it:

1. **The event record.** Every cartridge emits
   `{event, stage, band, retries, controlMode, personaPair, decision}` to one local writer. The
   writer picks an authored line. The record is the seam for a later live-dialogue connection;
   authored offline lines remain the fallback and the default. This is the review's
   `{event, hullBand, accuracyBand, retries, controlMode}` generalised by two fields.
2. **The frame bar.** A persistent bar on the frame edge, belonging to the tool and never to the
   fiction, in the Borland function-key pattern already proven in the binder: `F1 How this
   works`, `F2 Step out of character`, and a real `<a href>` back to Canvas. The no-penalty
   statement leads the panel. The exit exists with scripting disabled. This is the item-8
   distress button and it ships in the shell, so no cartridge can omit it.
3. **The record exporter.** One function turns the run's decision log into Markdown in the same
   shape the students already write (`# M<N> … Decision Record`, Round 1, Complication,
   Revision, Transfer). Copy button, download button, nothing transmitted.
4. **The profile switch.** `profile: "arcade" | "classroom"`. Classroom converts every
   depletion stake into a trade-off stake (§5.4) and keeps the run counter and the per-outcome
   delta, which the 2026-09-02 decision permits.
5. **Reduced motion, keyboard operation, contrast.** Already partly present; made mandatory.

The shell is internal tooling until a cartridge ships. Where it lives is §8.

---

## 4 · Product A — HTLL transfer simulations

These keep the CTS-285 pattern whole and change the world. They are *transfer practice*: the
student has no stake in the scenario, which is the same reason StudyTrack exists for M3.5.

Each one mirrors the mechanic the course already proved for that module. None replaces a
locked or built simulation. Each is optional and unplaced until the course owner places it.

| Module | CTS-285 mechanic (proved by) | HTLL scenario | Role | Constraint | Complication | Record |
|---|---|---|---|---|---|---|
| M2 | Investigation under limited evidence (M2 elicitation sim) | A platform operator on The Raft wants its docking-ledger "modernised". Four stakeholder voices: a harbour-master, a nomad captain, a Fixer who books berths, an AlgoCratic-Fujikara auditor | Systems Analyst | Three questions from seven; one is a solution-in-disguise (*which ledger technology?*), one is cosmetic | Berths are booked from boats with intermittent uplink; sessions drop mid-transaction | `# M2 Elicitation Decision Record` — same headings as the DataMan record; saved beside it, never over it |
| M3 | Constrained selection under limited capacity (M3.4 triage, M3.5 sprint) | ADS is contracted to ship a first release of a stream-safety tool for an Influencer's sponsor (Meridian Holdings) | Product Owner | Eight items, 13 points; two required defences | Capacity drops to 10; an accessibility finding makes one item release-critical | `# M3 Product Owner Decision Record`, with the *Transfer to DataMan* prompt at the end |
| M4 | Sprint readiness / design review (planned M4 sim) | A Nomad's boat-systems firmware story is top of the backlog with thin acceptance criteria, a wireframe that contradicts the story, an unresolved chrome dependency, and a vague Definition of Done | Scrum team | Commit, revise, split, or return | A security need surfaces; capacity is lost | `# M4 Sprint Readiness Record` — new; format to be fixed when the M4 sim is fixed |

Rules that do not bend for A:

- No named DataMan behaviour appears. The HTLL client is ADS or a named HTLL corporation; see
  decision 2 in §9 for which.
- The stakeholders speak in blockquote, as evidence. The machine voice appears only if the
  simulation is placed in an interstitial; on the default path there is no machine voice.
- Personas are not chosen in A. The student is the analyst. The HTLL cast are the stakeholders.
  Persona choice is Product B's mechanic, and mixing the two would make A a game.

M1 has no simulation in the course and A does not add one. M5–M8 are not planned.

---

## 5 · Product B — the arcade cabinet, one cartridge per module

### 5.1 The shape

A cartridge is one stage set for the shell. Its level structure is the CTS-285 pattern:

| Pattern step | In the cabinet |
|---|---|
| Brief | The sortie card: who you are, what the coast wants |
| Constraint | The stage rule: limited pings, limited weight, limited readiness |
| Choice | The play |
| Consequence | Exposed on screen and spoken by the handler or the Overlord |
| Decision Record | Exported Markdown at run end |
| Project Update | The closing line points at the graded artifact, not at another run |

The mechanics under the surface are the module's mechanics. The surface is HTLL.

### 5.2 The cartridges

| Module | Chain step | Cartridge | Reference | Mechanic underneath | What it drills |
|---|---|---|---|---|---|
| **M1** | System → Evidence | **Welcome to CoastOS 95** | Windows 95, the Office Assistant | An assistant keeps proposing solutions (*It looks like you're building a business solution!*). The player sorts each pop-up into symptom / root problem, and each item into people / process / technology / data. Wrong sorts spawn more pop-ups | Analysis vs design; a system is more than software; measurable outcomes over preferred features |
| **M2** | Evidence → Requirement | **Suspended, Coastal** | *Suspended* | The player is the analyst in the tank. The two chosen personas are the field units, and each perceives one channel. Every ping costs one of a limited budget. Evidence lands on a board; assumptions land on a separate board. Form a position, take the complication, revise | Investigation under limited evidence; evidence vs assumption; the solution-in-disguise question |
| **M3** | Story → Priority | **Hard Land, Rising** | *White Knuckle* | Vertical ascent through a flooding platform. Backlog items are the pack: each has weight (effort) and value. Each ledge is a sprint with a weight limit. Dependencies are anchors that must be placed first. The water rises: capacity drops, a keyboard-access item becomes load-bearing. Keep, remove, swap, defer, reopen | Constrained selection under limited capacity; defended deferral |
| **M4** | Priority → Readiness | **Breach Protocol** | *Trepang2*, *Hard/Wired Coast* | Before each sortie the player inspects the story on four doors: acceptance criteria, design evidence, dependency, Definition of Done. Slow-motion is the review pause. Launching an unready story is allowed, and the Overlord exploits exactly the gap that was skipped | Sprint readiness; commit, revise, split, return |
| M5–M8 | Plan → Build → Test → Review → Revise → Demonstrate | **Overlord Uplink** | *Hard/Wired Coast* | The shmup stages as the build loop; the Overlord as the review. **One-line sketch only** — M5–M8 are spine planning and this plan does not expand them | — |

M2 and M3 go first. Their mechanics are the two the course has already proved in a built
simulation, so the cartridge only has to carry them, not invent them.

### 5.3 Two personas

The player picks two of the four canonical playbooks. One is the **Lead** in the field; one is
the **Handler** on comms. This is the Handler → field-agent framing the HTLL prototype already
uses, and it is the *Coastal Control* voice in *Hard/Wired Coast* with a face.

The rule that keeps the pedagogy intact: **personas change what you see, hear, and can do.
They never change which analysis decision is defensible.** A stat gives richer evidence text,
a different move, a different line from the Handler. It does not make a wrong triage right.

| Stat | What it changes in a cartridge |
|---|---|
| Cool | Stakeholder evidence is fuller and the Handler's banter is warmer |
| Code | Systems evidence is fuller; the M4 dependency door opens faster |
| Tech | Design evidence is fuller; the M4 design door opens faster |
| Reflexes | Handling in the action stages; nothing in the decision stages |
| Body | Hull in the arcade profile; nothing in the classroom profile |

Six pairs. Each pair has authored lines for the six event moments the review named for the
Overlord: encounter begins, first node breaks, shield fails, hull first below 40 %, core at
50 %, victory or defeat. The pair's phase-trio crossing seeds the opening exchange.

The detailed persona rules, the six pair sheets, and the 4dF check node are HTLL material and
sit in `arcade/README.md` in that repository.

### 5.4 The classroom profile: stakes convert, they do not vanish

If a cartridge is launched from Canvas, the 2026-09-02 mechanics decision binds it. That
decision refuses hearts, lives, timers, XP, and rank because their only function is reward or
penalty. It does not refuse stakes. CTS-285 teaches prioritisation and trade-offs in character
already, so the profile switch converts each refused mechanic into the trade-off it was
standing in for:

| Arcade profile | Classroom profile | What it now teaches |
|---|---|---|
| Hull bar (depletes, then you lose) | **Capacity board** — a three-column kanban with a WIP limit. Damage pushes an in-progress item back to *blocked*. You do not die; you carry less | Capacity is finite and damage is rework |
| Score (six digits, only goes up) | **Shifts** — the Fate term. Each decision records the shifts it gained or cost, and the exporter writes them into the record as *the trade-off I accepted* | Every choice has a cost that can be named |
| Timer / rising tide (speed pressure) | **Complication rounds** — turn-based. The water rises one round after each decision, and the complication changes the choice set, never the clock | Constraints change; plans get revised |
| Lives / retries | **Compel** — the Lead's Trouble aspect is compelled. Accept it: gain a Fate point and take the complication. Refuse it: spend one. Either way the run continues | Failure is a trade, not an ending |
| Rank | **A perk with a plus and a minus** — a persona trait stated as a Fate aspect, invokable and compellable, chosen at the sortie card | Strengths carry exposures |

Fate's invoke-and-compel loop is already a trade-off engine, and the personas already carry
Trouble aspects (*My Boat Is Falling Apart and Repairs Cost More Than I Make*). The classroom
profile leans on that instead of on a health bar.

What stays under either profile: the run counter, the per-outcome delta over the last run, a
comprehension display that can fall and reads from evidence of the skill, and a closing line
that exits to the graded artifact.

**The fallback is the demonstration label.** Where a stake will not convert cleanly, the
cartridge ships with a stated frame: *this demonstrates course material; it is not course
material.* Success and failure are then shown as a trade-off the student reads rather than one
they are measured on. The frame bar carries the label so it is never a matter of tone.

Build to the classroom profile first and add the arcade profile on top; the other order
produces a game with a lesson glued on.

---

## 6 · The shared data format

The HTLL prototype's story JSON is the seed: a scene dictionary, messages with a speaker,
choices with conditions and effects, flat additive state. Three additions make it carry the
cabinet:

1. A **`check` node** — `{stat, difficulty, on_style, on_success, on_tie, on_fail}` — using the
   four outcome tiers the core moves sheet defines and the Twine scene already implements. The
   prototype pre-branches every roll into separate scenes; the node removes that.
2. A **`stage` node** for the real-time stages, holding the stage rule, the spawn table, and
   the event moments.
3. A **`record` block** naming which flags and choices the exporter writes into which heading
   of the decision record.

Two prototype conventions get normalised on the way in: stress sign (the prototype damages on a
negative number) and the `scene_type` field (declared, never read). The `vars` block the scene
format specifies was never implemented and is dropped rather than carried.

The format is defined once, in HTLL, and Product A uses the same file shape with no `stage`
nodes.

---

## 7 · The aesthetic system

Two registers, one frame:

- **The frame is the 1977 device.** LED readout, amber keys on a blue panel, brushed bezel,
  ribbed rails, and the cosmic booklet cover for the sortie card. The design notes already state
  the value of this frame: a readout that fits one line cannot become a scoreboard.
- **The field is the CRT.** *Hard/Wired Coast*'s scanlines, cyan on void, condensed type.
- **The assistant is Windows 95.** Grey dialog, title bar, close box, *Did you know…*. It is the
  voice of the wrong idea in M1 and the tip surface everywhere else. It is never the exit; the
  exit is the frame bar.

Each reference contributes one thing and no more: *White Knuckle* gives M3 its verticality and
its rising threat; *Trepang2* gives M4 its breach-and-pause; *Suspended* gives M2 its status
board and its one-sense agents. None of them supplies art, which is drawn in the HTLL house
style (ink and duotone).

Persona palettes come from HTLL's `CLAUDE.md`: Infiltrator orange/teal, Influencer magenta/navy
with gold, Nomad cyan/purple. **The Fixer has no palette on record** and needs one before the
Fixer's pair sheets are drawn.

The five panels of the *It Looks Like You're Building a Business Solution* infographic are
rebuilt as Mermaid: a system is people + process + technology + data; value comes from solved
problems; symptom vs root; analysis vs technical solution; deployment is organisational change.
The cartridges run offline in one file, so Mermaid is rendered to inline SVG at build time, not
loaded from a CDN. The same SVGs can go to Canvas pages through the compositor's existing route.

---

## 8 · Where things live

| Thing | Repository | Path |
|---|---|---|
| This plan; any simulation or cartridge the course owner places for students | `AMLW05/cts-285-course-simulations` | `planning/`; by module, as the existing arcades are |
| Governance, decisions, build guides, Canvas launch pages | `AMLW05/cts-285_SOURCE` | `planning/`, `module-XX/final-build/` |
| Persona rules, pair sheets, cartridge format, reference build, review | `norrisaftcc/game-high-tech-low-lives` | `arcade/` |
| The shell and the cartridges while they are HTLL products | `norrisaftcc/game-high-tech-low-lives` | `arcade/cabinet/`, `arcade/cartridges/` |

The audience test from `REPOSITORY-OWNERSHIP.md` decides every move: a student opens it from
Canvas → the simulations repository; otherwise not. Nothing runnable goes into this
repository.

---

## 9 · Decisions this plan needs

None of these are the plan's to make.

1. **Kayfabe items 2, 3, 4, and 8** (`KAYFABE-MEETING-2026-09-03.md`). Whether a hosted arcade
   may carry in-character framing; where interstitials sit; whether one beside M2 touches the
   lock; who builds the Canvas-side distress button. Until these are decided, every product here
   is an HTLL product and is not placed.
2. **The client's name in Product A.** The two-product rule reserves *ADS — Algorithmic Data
   Solutions Ltd.* for the next corporate scenario. The HTLL world has its own corporations.
   Recommended: ADS is the client and is placed in the HTLL world as a contractor; Meridian
   Holdings and AlgoCratic-Fujikara are its customers. That keeps one corporate name in the
   course and gives it a home.
3. **Shodann.** In HTLL, *Shodann* is the player's handle for the Infiltrator. In CTS-285,
   *SHODANN* is the machine narrator. Both names cannot mean both things in one interstitial.
   Recommended: the machine narrator in the cabinet is *The Algorithm*, HTLL's own antagonist,
   and SHODANN stays a person.
4. **Which conversion in §5.4 is the default.** Capacity board, compel, and shifts are the
   plan's picks. The demonstration label is the fallback. Confirm the picks or choose others.
5. **HTLL Phase 3.** The cabinet is technical implementation, which HTLL has deferred. The
   plan treats a single-file HTML cartridge as within the *Hard/Wired Coast* precedent and
   outside the React veto. Confirm.

---

## 10 · Sequence and size

| Sprint | Work | Output |
|---|---|---|
| 1 | Product 0: the nine review items on *Hard/Wired Coast*; the event record; the frame bar; the exporter; the profile switch | A playable shell; a playtest note with human notes this time |
| 2 | M2 *Suspended, Coastal* and M3 *Hard Land, Rising*, in parallel; six pair sheets for the personas | Two cartridges; two sample decision records |
| 3 | Product A for M2 and M3, on the same data format | Two transfer simulations; two sample records |
| 4 | M1 *CoastOS 95*; the Mermaid rebuild of the five panels | One cartridge; five SVGs reusable in Canvas |
| 5 | M4 *Breach Protocol* and the M4 simulation, when the M4 sim design is fixed | Held until M4 is stable |

Each sprint's deliverable is one file that opens from `file://` with no network. The review
noted that the workspace browser runner could not launch; the sprint-1 playtest note must come
from a human on a phone, which is what the build is for.

---

## 11 · Delegation map

The three products are parallel because their inputs are disjoint. Each row is one sonnet
subagent thread, launched with the named files as its whole context. The lead session holds the
plan, merges, and runs the checks; the threads do not touch each other's files.

| Thread | Model | Input files | Output | Done when |
|---|---|---|---|---|
| **shell-repair** | sonnet | `arcade/hardwired-coast/index.html`, `arcade/hardwired-coast/REVIEW-2026-09-10.md` | `arcade/cabinet/index.html` with the nine review items, the event record, the frame bar, the exporter, the profile switch | Opens from `file://`; both touch profiles work on a phone; the Overlord falls in 20–30 s at 60 % accuracy; F2 exits with scripting disabled |
| **pair-sheets** | sonnet | The four `*_playbook_v2.md`, `core_moves_sheet.md`, `phase-trio.md`, `arcade/README.md` §Personas | Six pair sheets in `arcade/personas/`, each with the six event lines and the opening exchange | Every line under 90 characters; no line names a DataMan behaviour; the Fixer has a palette |
| **cartridge-m2** | sonnet | `SIMULATION-ARCHITECTURE-M2-M4.md` §M2, the M2 sim build guide, `arcade/README.md` §Format, *Suspended* notes | `arcade/cartridges/m2-suspended-coastal.json` and its stage module | A run exports a record with the M2 headings; three of seven pings; one solution-in-disguise |
| **cartridge-m3** | sonnet | `SIMULATION-ARCHITECTURE-M2-M4.md` §M3, the M3.5 sim data, `arcade/README.md` §Format, *White Knuckle* notes | `arcade/cartridges/m3-hard-land-rising.json` and its stage module | 13 → 10 capacity; keyboard item becomes load-bearing; keep / remove / swap / defer / reopen all reachable |
| **sim-a-m2 / sim-a-m3** | sonnet | Same as the cartridge rows, minus the reference notes | Two transfer simulations on the same format with no `stage` nodes | Record shape matches the DataMan record heading for heading |
| **mermaid-panels** | sonnet | The five-panel infographic description in §7 | Five Mermaid sources and five inline SVGs | Each SVG passes `compcheck.py` when wrapped in a Canvas fragment |
| **playtest-note** | human | The shell on a phone | `arcade/cabinet/PLAYTEST-<date>.md` | Not delegable |

Merge order: shell-repair first, because every cartridge loads into it. Pair sheets and the two
cartridges can start on the reference build and rebase onto the repaired shell. The lead runs
`compcheck.py` on anything bound for Canvas and reads every decision record the threads export
against the student templates before merging.

## 12 · Contradictions found in the sources

Recorded so they are not rediscovered. None is resolved here.

- HTLL's setting is pelagic in `build_notes.md` and the v0 scene, and orbital in the v2 title
  page (Golgotha as a toxic-atmosphere colony; Sidereal Station at Lagrange-4). The cabinet
  follows the ocean.
- HTLL's Face, Hacker, and Enforcer playbooks exist but are not canonical; the Hacker exceeds
  the +3 stat cap. The cabinet uses the four canonical playbooks only.
- The M2 elicitation simulation build guide's technical-source line still points at the legacy
  `AMLW05/cts-285_sim` branch rather than `cts-285-course-simulations/m2/stakeholder-elicitation/`.
- `DECISIONS.md` dates DataMan to 1977; the locked M2 overview page says 1979. The device shipped
  in 1977. The page is locked; the note is recorded.
- The HTLL prototype's `scene_format.md` specifies `vars`, `threat_scan`, and `building_intel`;
  the engine implements none of them.
