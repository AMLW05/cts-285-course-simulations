# CTS 285 — Module 1 Exit Tickets (Question Source)

Source of truth for the QTI packages. Edit this file, then re-run `build_qti.py`.

**Format contract** (the parser depends on it):

- `## QUIZ: <id> | <title>` starts a quiz. `<id>` becomes the zip and folder name.
- `> <text>` lines directly under a quiz heading become the quiz description.
- `### Q<n>. <stem>` starts an item.
- `- [x]` marks the correct option. `- [ ]` marks a distractor.
- `  - FB: <text>` on the line after an option is that option's feedback.
- Blank lines separate items. Do not use other Markdown inside stems or options.

Every item is multiple choice with one correct answer. Every option carries feedback.

---

## QUIZ: cts285-m1-4-exit-ticket | 1.4 Exit Ticket — The Systems Development Life Cycle

> Five questions. Answer each one to confirm that you can identify the four SDLC phases and the work that belongs to each phase. Feedback appears after you submit.

### Q1. Which statement describes progressive refinement in the SDLC?

- [x] Each phase adds detail to the work completed in the previous phase.
  - FB: Correct. Projects do not begin with every detail known. The solution becomes clearer and more detailed as the project moves through each phase.
- [ ] The project team defines every detail before the Planning phase starts.
  - FB: Incorrect. If the team knew every detail at the start, the four phases would not be necessary. Detail is added phase by phase.
- [ ] The team repeats each phase until the budget is spent.
  - FB: Incorrect. Refinement describes increasing detail, not repetition. Each phase has a defined purpose and a defined end.
- [ ] The team removes requirements at the end of each phase.
  - FB: Incorrect. Refinement adds detail. It does not remove work that earlier phases produced.

### Q2. The college asks whether the parking permit problem is worth solving and whether the project can realistically be completed. Which SDLC phase includes these questions?

- [x] Planning
  - FB: Correct. Planning answers the question "Should we build it?" The team examines value, feasibility, resources, and timeline before the project is approved.
- [ ] Analysis
  - FB: Incorrect. Analysis answers "What should it do?" Analysis starts after the project is approved.
- [ ] Design
  - FB: Incorrect. Design answers "How will it work?" The team cannot design a system that is not yet approved.
- [ ] Implementation
  - FB: Incorrect. Implementation builds, tests, and launches the system. It is the last phase, not the first.

### Q3. The systems analyst interviews students, meets with Campus Police, and observes how permits are issued today. Which SDLC phase includes this work?

- [x] Analysis
  - FB: Correct. Analysis investigates the current process. The analyst collects information to define what the future system must accomplish.
- [ ] Planning
  - FB: Incorrect. Planning decides whether to approve the project. The detailed investigation happens after approval.
- [ ] Design
  - FB: Incorrect. Design begins after the requirements are identified. The analyst is still identifying them here.
- [ ] Implementation
  - FB: Incorrect. Implementation builds the system. No system exists yet at this point in the project.

### Q4. The team decides what the student screens will look like, what information the system stores, and how Campus Police will search permits. Which SDLC phase includes these decisions?

- [x] Design
  - FB: Correct. Design produces a detailed blueprint that developers follow during Implementation.
- [ ] Analysis
  - FB: Incorrect. Analysis identifies what the system must do. Design decides how the system will do it.
- [ ] Planning
  - FB: Incorrect. Planning approves the project and creates the project plan. It does not specify screens or stored data.
- [ ] Implementation
  - FB: Incorrect. Implementation builds what Design specified. These decisions come first.

### Q5. Which activity belongs to the Implementation phase?

- [x] Training the users of the new permit system
  - FB: Correct. Implementation includes building, testing, training, launching, and ongoing support.
- [ ] Interviewing students about the current permit process
  - FB: Incorrect. Interviews collect requirements. That work belongs to Analysis.
- [ ] Deciding whether the project provides enough value to approve
  - FB: Incorrect. That decision belongs to Planning.
- [ ] Deciding how permit requests will be approved
  - FB: Incorrect. That decision belongs to Design, which produces the blueprint for Implementation.

---

## QUIZ: cts285-m1-5-exit-ticket | 1.5 Exit Ticket — Reading a System Like a Systems Analyst

> Five questions. Answer each one to confirm that you can apply the four-step reading process and separate observations from assumptions. Feedback appears after you submit.

### Q1. A systems analyst receives documentation for an unfamiliar system. What does the analyst do first?

- [x] Examine the documentation to understand what the system does and who uses it
  - FB: Correct. Analysts begin by understanding the system that already exists. Understanding comes before any change.
- [ ] List the features that the system is missing
  - FB: Incorrect. Missing features are a conclusion. You cannot identify them before you understand the current system.
- [ ] Begin redesigning the parts of the system that look inefficient
  - FB: Incorrect. Redesign happens much later, and only after the analyst understands the system and its evidence.
- [ ] Learn the steps that operate the system
  - FB: Incorrect. That is reading like a user. An analyst reads for evidence about how the system works.

### Q2. A statement records that a coffee shop uses Square to process payments. The documentation does not mention any payment software. How do you classify this statement?

- [x] An assumption, because no evidence supports it
  - FB: Correct. An assumption is a conclusion made without enough evidence. Record it as an assumption or note that more information is needed.
- [ ] An observation, because payment software is common in coffee shops
  - FB: Incorrect. Common practice is not evidence. An observation must be supported by the documentation.
- [ ] An observation, because the shop must process payments somehow
  - FB: Incorrect. The shop does process payments, but the specific product named here is not supported by evidence.
- [ ] A verified fact, because it can be checked later
  - FB: Incorrect. A statement that still needs checking is not yet verified. Do not record it as a fact.

### Q3. Which step of the four-step reading process requires you to support every conclusion with evidence found in the documentation?

- [x] Verify
  - FB: Correct. Verify is the third step. Every conclusion must point to evidence in the documentation.
- [ ] Observe
  - FB: Incorrect. Observe is the first step. You read carefully and do not jump to conclusions yet.
- [ ] Identify
  - FB: Incorrect. Identify is the second step. You locate evidence about users, purpose, inputs, outputs, and processes.
- [ ] Document
  - FB: Incorrect. Document is the fourth step. You record what you know and identify what cannot yet be determined.

### Q4. An analyst asks, "What happens to the information after it enters the system?" Which category does this question examine?

- [x] Processing
  - FB: Correct. Processing describes what the system does to information after the information enters the system.
- [ ] Inputs
  - FB: Incorrect. Inputs describe what information enters the system, not what happens to it afterward.
- [ ] Outputs
  - FB: Incorrect. Outputs describe what information the system returns.
- [ ] Feedback
  - FB: Incorrect. Feedback describes how the system responds to the user.

### Q5. You cannot point to evidence that supports a conclusion. What does the professional rule require you to do?

- [x] Identify it as an assumption, or note that more information is needed
  - FB: Correct. This rule keeps the case file honest. Unknowns are useful findings, not failures.
- [ ] Record it as a fact and mark it for review later
  - FB: Incorrect. Do not record an unsupported conclusion as a fact. That is the exact error the rule prevents.
- [ ] Remove the conclusion from your notes completely
  - FB: Incorrect. The conclusion still has value as an assumption or as an identified unknown. Label it instead.
- [ ] Ask another student whether the conclusion sounds correct
  - FB: Incorrect. Agreement is not evidence. The conclusion must be supported by the documentation.

---

## QUIZ: cts285-m1-6-exit-ticket | 1.6 Exit Ticket — Guided Document Analysis: The Story of DataMan

> Five questions. Answer each one to confirm that you can read product documentation as a systems analyst. Feedback appears after you submit.

### Q1. What is your objective when you analyze the DataMan documentation in this lesson?

- [x] Identify evidence and support conclusions about the system
  - FB: Correct. The objective is to find evidence, support conclusions, and separate observations from assumptions.
- [ ] Redesign the product so it works better
  - FB: Incorrect. Redesign is not the objective of this activity. Analysts understand a system before they change it.
- [ ] List the improvements the product needs
  - FB: Incorrect. Improvements are conclusions about change. This activity builds the evidence that comes first.
- [ ] Learn the steps that operate the product
  - FB: Incorrect. That is reading like a user. Read for evidence about how the system works instead.

### Q2. Why does the lesson ask you to read "The Story of DataMan" twice?

- [x] The first reading builds familiarity, and the second reading collects evidence
  - FB: Correct. Professional analysts rarely understand a system after a single reading. Each reading has a different job.
- [ ] The second reading checks the spelling and grammar of the document
  - FB: Incorrect. The second reading looks for evidence about how the system works, not for writing errors.
- [ ] The first reading collects evidence, and the second reading confirms your opinion
  - FB: Incorrect. The order is reversed, and opinion is not part of the process. Conclusions come from evidence.
- [ ] Two readings are required before you may ask questions
  - FB: Incorrect. There is no such rule. The two readings serve familiarity and evidence.

### Q3. How did the analyst determine the primary purpose of DataMan?

- [x] The analyst combined repeated references from several parts of the documentation
  - FB: Correct. Repeated references to learning mathematics, practicing skills, and immediate feedback together support the conclusion.
- [ ] The analyst found one sentence that began, "The purpose of this system is..."
  - FB: Incorrect. Documentation rarely states purpose directly. The analyst builds the conclusion from combined evidence.
- [ ] The analyst used personal experience with similar math products
  - FB: Incorrect. Personal opinion is not evidence. The conclusion must come from the documentation.
- [ ] The analyst asked the product's users what the purpose was
  - FB: Incorrect. In this activity the documentation is the only source of evidence.

### Q4. The analyst identified students, teachers, parents, and independent learners as users. Why did the analyst not list any other user groups?

- [x] The documentation provides no evidence of additional users
  - FB: Correct. Analysts record only what evidence supports. Groups without evidence are not added to the case file.
- [ ] Four user groups is the maximum an analyst records
  - FB: Incorrect. There is no limit on user groups. The evidence determines how many you record.
- [ ] Other user groups are always identified during the Design phase
  - FB: Incorrect. Users are identified from available evidence whenever that evidence appears.
- [ ] The other user groups were not important enough to record
  - FB: Incorrect. The analyst did not judge importance. No evidence of other groups existed.

### Q5. Which statement about DataMan is an assumption rather than an observation?

- [x] DataMan is the most effective mathematics product available today
  - FB: Correct. Nothing in the documentation compares DataMan with other products. This is a conclusion without evidence.
- [ ] The documentation refers to students as users of the product
  - FB: Incorrect. This is an observation. Students are referenced in the documentation.
- [ ] The documentation refers to immediate feedback during practice
  - FB: Incorrect. This is an observation. Immediate feedback is referenced in the documentation.
- [ ] Teachers appear among the people who interact with the product
  - FB: Incorrect. This is an observation. Teachers are referenced in the documentation.
