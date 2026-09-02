# CTS 285 — Module 2 Exit Tickets (Question Source)

Source of truth for the QTI packages. Edit this file, then run:

    python3 ../m1/build_qti.py m2-exit-tickets-source.md --out qti/

**Format contract** (the parser depends on it):

- `## QUIZ: <id> | <title>` starts a quiz. `<id>` becomes the zip and folder name.
- `> <text>` lines directly under a quiz heading become the quiz description.
- `### Q<n>. <stem>` starts an item.
- `- [x]` marks the correct option. `- [ ]` marks a distractor.
- `  - FB: <text>` on the line after an option is that option's feedback.
- Blank lines separate items. Do not use other Markdown inside stems or options.

Every item is multiple choice with one correct answer. Every option carries feedback.

**Scope.** M2 already assesses MLO 2.1 (Requirement Triage Lab) and MLO 2.3
(Requirement Repair Lab). MLO 2.2 — elicitation — has no Canvas-visible check.
This fills that one gap. Deliberately one ticket, not four.

**Product.** The 1977 TI DataMan, modernized to Python/Flask. Evidence base:
`m1/dataman-manual.md`, `m1/DataMan_US.pdf`. Stakeholders are teachers,
parents, learners, and the manual itself.

**Relationship to the arcade.** These are *different instances of the same
discriminations* the DataMan Field Check drills. Same judgments, new surfaces —
a student who drilled the skill transfers; one who memorized an item does not.
None of these five appears in the arcade bank.

**Placement.** After `M2.3 — DataMan Elicitation Case` and before the
Simulation. Consolidate the moves, then do it under pressure.

**Points.** 5.0 total, matching the Module 1 exit tickets.

---

## QUIZ: cts285-elicitation-exit-ticket | Exit Ticket — Requirements Elicitation

@attempts: -1
@shuffle: true
@points: 1.0

> Five questions on finding the need behind a request. You may retake this. Feedback appears on every option, so read the explanation even when you answer correctly.

### Q1. A teacher who used DataMan in her classroom tells you, "The kids got frustrated with it." What has she given the analyst?

- [x] A concern that establishes investigation is needed, but not yet a requirement.
  - FB: Correct. Frustrated at what, at which point, and compared with what? A concern is evidence that something is worth looking into. It is not a finished requirement.
- [ ] A usability requirement, since frustration is a usability problem.
  - FB: Too early. Usability may turn out to be the area, but nothing here names a task or a condition anyone could verify.
- [ ] An assumption, since she has not shown you the frustration happening.
  - FB: Useful instinct, and it goes one step too far. She is reporting what she observed in her own classroom. Treat it as evidence that investigation is warranted, not as something to set aside.
- [ ] A proposed solution, because "frustrated" implies the interface needs changing.
  - FB: Nothing is proposed here. She described an outcome she saw, not a mechanism she wants.

### Q2. A parent says the score display "discourages" their child. Which follow-up gathers evidence rather than manufacturing agreement?

- [x] "What does your child do right after the score appears?"
  - FB: Correct. It asks for observed behavior at a specific moment. What they do next is the evidence; "discouraged" is the interpretation.
- [ ] "Would it help if we hid the score until they asked for it?"
  - FB: Too early. It proposes a design before anyone knows what about the score lands badly — the number, the comparison, or the moment it appears.
- [ ] "Wouldn't it be better to show only the number they got right?"
  - FB: Leading. It hands the parent your conclusion and asks them to agree with it. Agreement gathered this way is not evidence.
- [ ] "How many problems does your child usually get wrong?"
  - FB: Useful eventually. It measures performance when the reported problem is about response to feedback.

### Q3. You need to know how many problems the Memory Bank can hold. What is the right first move?

- [x] Read the manual. It states the limit in both registers.
  - FB: Correct. Ten problems, said plainly in the Story and again in the Operating Notes. Check what you already hold before you spend anyone's time.
- [ ] Interview a teacher who used the device.
  - FB: Useful for how the feature was used in practice. For a documented capacity it spends goodwill on something already written down.
- [ ] Observe a child loading problems into it.
  - FB: Too early. Observation is expensive and it answers questions the document cannot. This is not one of them.
- [ ] Record it as an open question for the project team.
  - FB: Documenting uncertainty is a good habit and this is not uncertain. An open question that the source answers weakens every real one beside it.

### Q4. During planning someone writes: "DataMan should give hints when a learner is stuck." Classify that statement.

- [x] A need that is not yet a requirement — "stuck" has no definition.
  - FB: Correct. Stuck after one wrong answer, after thirty seconds, after two attempts? Each is a different system. The need is real and the statement is not testable yet.
- [ ] A functional requirement, since it describes something the system does.
  - FB: Useful reading — it is shaped like behavior. It cannot be verified until someone says what stuck means.
- [ ] A proposed solution, because hints are one possible mechanism.
  - FB: Close, and the sharper problem is the undefined trigger. A hint is a reasonable response to being stuck; nobody has said when that is.
- [ ] Evidence, because it came from the project team.
  - FB: Who said it does not make it evidence. Evidence is what a source established, not what a participant proposed.

### Q5. Evidence shows learners often stop after a wrong answer instead of trying again. What confirms you are ready to write a requirement?

- [x] You can state what observable result would show the problem has been addressed.
  - FB: Correct. If you cannot say how the team would later tell whether the need was met, the requirement is not testable yet, whatever else is true about it.
- [ ] The teacher who raised it agrees with your wording.
  - FB: Useful, and agreement is not verification. A stakeholder can approve a statement that is still vague or still a solution in disguise.
- [ ] You have decided the system will offer a second attempt automatically.
  - FB: Too early. That is a mechanism, and the 1977 device already had one — which is worth knowing before you require it again.
- [ ] You have observed enough learners to be confident the pattern is real.
  - FB: Good evidence discipline, and it establishes that the problem exists. It does not by itself make the requirement clear or testable.
