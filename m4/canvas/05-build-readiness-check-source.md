> **SUPERSEDED / WITHDRAWN SUPPORT COPY**  
> Retained only for course-development history. This file is **not** part of the current Module 4 Canvas sequence. Use `AMLW05/cts-285_SOURCE` and `module-04/M4-CANVAS-SEQUENCE.md` as the authoritative source.

# M4 Build Readiness Check — Canvas New Quizzes Source

Purpose: verify transfer to new situations after the Design Studio. Keep this short and auto-graded. Do not reuse the student's own project evidence.

Recommended: 8 points total. No True/False. Avoid fill-in-the-blank. Use stimulus, ordering, matching, and categorization.

## Stimulus 1 — Answer Flow Change
A team has a working two-attempt flow. A new requirement says a learner may leave after the first wrong attempt and return later. The current design stores `try_number` only in the browser interface. Attempt records are written only when the problem is completed.

### Q1 — Multiple Choice — 1 point
Which design question should the team answer before coding the change?

A. Which browser framework should manage the retry screen?
B. What state must survive interruption so the learner can resume without changing the two-attempt rule? **[Correct]**
C. Which color should identify a resumed problem?
D. Should the retry button move above the answer field?

Feedback: The implementation question is about durable state and behavior across interruption, not interface technology or visual treatment.

### Q2 — Categorization — 2 points
Sort each item into the layer where it primarily belongs.

**Interface**
- Display “Try again” after the first miss.
- Show the correct answer after the business rule returns a reveal outcome.

**Business logic**
- Decide whether another attempt is allowed.
- Decide whether the answer may be revealed.

**Data boundary**
- Save an incomplete attempt/session state so it can be restored later.
- Retrieve prior attempts for the resumed problem.

## Stimulus 2 — Practice Set Review
A curator can create a practice set containing up to ten problems. The current model stores a comma-separated list of problem IDs on the PracticeSet record. A learner's final score is stored, but individual attempts are not.

### Q3 — Matching — 2 points
Match each design concern to the evidence most likely to expose it.

- Can the 10-problem rule be enforced? → Constraint/business-rule test
- Can a curator retrieve which problems were missed? → Retrieval query traced through the data model
- Is the learner given a dead end after a second miss? → Interaction/state flow
- Does a reusable rule live only inside one screen? → Layer/component responsibility review

### Q4 — Ordering — 1 point
Put the design reasoning loop in the most useful order.

1. Frame the question
2. Select/create evidence
3. Make a decision
4. Inspect the consequence
5. Evaluate the result
6. Revise if needed
7. Identify the next question

## Stimulus 3 — Ready or Not?
A story says, “As a curator, I want to review learner progress.” During design, the team discovers that the requested view now includes learner selection, date filtering, missed-problem details, and different permissions for parents and teachers. Permission rules have not been confirmed.

### Q5 — Multiple Choice — 1 point
What is the most defensible build-readiness disposition?

A. Proceed; developers can decide permissions during implementation.
B. Split/refine the work and gather evidence about permission rules before committing the affected slice. **[Correct]**
C. Delete the story because it became too large.
D. Proceed unchanged because the original user story is already approved.

### Q6 — Multiple Choice — 1 point
Which statement best demonstrates evidence-based revision?

A. “We changed the design because the new one looks cleaner.”
B. “We added a dashboard because dashboards are standard.”
C. “The retrieval test showed that final score alone cannot answer which problems were missed, so we revised the model to retain attempt-level evidence.” **[Correct]**
D. “We kept the original model because changing it would take more work.”

## Alignment
- Q1: MLO 4.1 — frame an implementation-relevant design question.
- Q2–Q3: MLO 4.2 — connect interaction, behavior, architecture, and data evidence.
- Q4–Q6: MLO 4.3 — evaluate consequences, revise, and determine readiness.
