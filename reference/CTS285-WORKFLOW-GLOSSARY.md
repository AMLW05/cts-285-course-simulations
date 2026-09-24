# CTS-285 Workflow Glossary

**Student-shareable reference.** This copy is exported from the private CTS-285 source repository. If a project-specific definition ever differs from the private source, the private source wins and this copy should be refreshed.


This guide explains the words and working habits used in the CTS-285 build. It is written so it can be shared with students, instructors, designers, and technical collaborators.

It is **not a list of GitHub commands to memorize**. The goal is to understand what is happening when people work together on a project and how evidence moves from an idea or problem to a finished, reviewed change.

---

## 1. The collaboration loop

Our normal change process looks like this:

> **Need / problem / idea → Issue → Branch → Change → Commit → Pull Request → Review → Revision → Checks → Merge → Verification → Close**

Sometimes a step loops:

> **PR → Review comment → Revision → New commit → Re-check → Review again**

That back-and-forth is normal. It is not evidence that the first attempt “failed.” It is how collaborative work becomes inspectable before it becomes part of the shared project.

### Step 1 — Need, problem, or idea

Work begins because something needs to happen:

- a defect was found;
- a requirement changed;
- a page needs to be built;
- a technical question must be answered;
- a workflow needs verification;
- a decision needs to be recorded.

Do not begin by changing random files. First understand **what problem the change is supposed to solve**.

### Step 2 — Issue

An **issue** is the record of the work to be understood, decided, built, fixed, or verified.

A useful issue answers:

- What is happening?
- Why does it matter?
- What would count as complete?
- Who owns the next action?
- Is this a design decision, technical question, defect, verification task, or reminder?

An issue can stay open intentionally. For example, an end-of-course verification issue may be fully defined today but remain open because the closure condition is “after the current cohort finishes.”

### Step 3 — Branch

A **branch** is a safe line of work separated from the shared `main` branch.

Think of it as:

> “I am working on this change without rewriting everyone else’s current copy.”

A branch should have a clear purpose. One focused change is easier to review than a branch carrying unrelated work.

### Step 4 — Change

Files are created, edited, moved, or retired on the branch.

The important question is not only **“Does this look right?”** but also:

> “Does this change preserve the contracts that other parts of the project already depend on?”

That is why CTS-285 often talks about boundaries, seams, artifacts, paths, and evidence.

### Step 5 — Commit

A **commit** is a named snapshot of a change.

A good commit says what changed in a way another person can understand later.

Commits give us history. They let us answer:

- When did this change happen?
- What changed with it?
- What did the project look like before it?
- Which change introduced or fixed a problem?

### Step 6 — Pull Request (PR)

A **pull request**, usually shortened to **PR**, asks to merge a branch into the shared project.

A PR is more than “please accept my code.” It is a review surface. It should explain:

- what changed;
- why;
- what evidence supports it;
- what was tested;
- what remains intentionally out of scope.

### Step 7 — Review

A reviewer reads the PR before it becomes part of `main`.

Review may produce:

- approval;
- questions;
- requested changes;
- a finding that the requirement itself is unclear;
- evidence that the change affects something outside its original scope.

Review comments are part of the work. The author may revise the branch and push additional commits to the same PR.

### Step 8 — Checks

Automated checks may run on the PR.

In this project, checks can examine things such as:

- house-style regressions;
- whether generated artifacts can be rebuilt;
- whether a manifest still matches the files it claims to organize;
- whether tests still pass.

A **green check** means that check passed. A **red check** means something needs attention. A red check is evidence, not a diagnosis by itself; read what actually failed.

### Step 9 — Merge

To **merge** means to combine the reviewed branch into the shared branch, usually `main`.

Once merged, the change becomes part of the project’s shared history.

### Step 10 — Verification

A merge does not always prove the real environment works.

Some changes require later verification such as:

- checking the live Canvas course;
- running commands in a student Codespace;
- opening a hosted simulation in a browser;
- confirming a link from Canvas reaches the correct runtime.

That is why some issues remain open after a PR merges.

### Step 11 — Close

An issue closes when its **closure condition** is actually met.

“PR merged” and “issue complete” are often—but not always—the same event.

---

## 2. Core Git and GitHub vocabulary

| Term | What it means here |
|---|---|
| **Repository / repo** | A versioned project space containing files, history, issues, PRs, and automation. |
| **Main** | The shared branch representing the accepted project state. |
| **Branch** | A separate line of work used to develop a focused change safely. |
| **Commit** | A recorded snapshot of changes with a message explaining what changed. |
| **Clone** | A local copy of a repository. |
| **Checkout / switch** | Move your working copy to a particular branch or commit. |
| **Diff** | The exact line-by-line difference between two versions. |
| **Push** | Send local commits to the remote GitHub repository. |
| **Pull** | Bring remote changes into the local working copy and integrate them. |
| **Fetch** | Download information about remote changes without automatically integrating them. |
| **Issue** | A tracked problem, question, task, decision, verification, or reminder. |
| **Assignee** | The person responsible for the issue’s next action. |
| **Pull Request (PR)** | A request to review and merge one branch into another. |
| **Review** | Examination of a PR before merge; may include questions or requested changes. |
| **Merge** | Combine reviewed branch changes into the shared branch. |
| **Merge conflict** | Git cannot automatically combine competing edits and a human must decide the final version. |
| **Workflow / GitHub Action** | Automated work GitHub runs after an event such as a PR or push. |
| **CI (Continuous Integration)** | Automated checks that evaluate changes before or after merge. |
| **Green / red** | Informal shorthand for passed / failed automated checks. |
| **Milestone** | A phase or goal used to group related work and track progress over time. |
| **Closeout** | Final verification, parity, cleanup, documentation, and handoff after the main design/build work is complete. |

---

## 3. Words we use for project structure

### Artifact

An **artifact** is something the work produces and carries forward.

Examples:

- a decision record;
- a backlog;
- a schema document;
- a test;
- a review record;
- a handoff package.

An artifact is stronger than “I did the activity” because someone else can inspect it later.

### Persistent artifact

A **persistent artifact** is intentionally kept across modules or phases.

CTS-285 uses persistent artifacts so the project does not reset every week. Later work should be able to point back to earlier evidence.

### Source of truth

A **source of truth** is the authoritative place to resolve a question when multiple copies exist.

It does not mean “this file can never be wrong.” It means that when two copies disagree, the project has a stated rule for which source governs until the discrepancy is reconciled.

### Authority hierarchy

An **authority hierarchy** tells collaborators which record wins when documents disagree.

This is important because project records are created at different times. A later decision may deliberately supersede an earlier plan.

### Spine

A **spine** is the continuous structure that connects work across a project.

In CTS-285, “spine” is used in two related ways:

- **project spine** — DataMan and its evidence carry across modules;
- **implementation spine** — responsibility boundaries continue from prototype to Flask, testing, persistence, and handoff.

The point is continuity: the later module consumes something real from the earlier one.

### Seam / boundary

A **seam** or **boundary** is the place where one responsibility meets another.

A good boundary lets one side change without forcing unrelated changes everywhere else.

For example, if storage can change behind a stable `load_state()` / `save_state()` interface, tests can determine whether behavior survived the storage change.

### Scaffold

A **scaffold** is temporary structure that supports someone while a skill is new.

Examples include:

- templates;
- prompts;
- supplied examples;
- controlled failure cases;
- guided checklists.

### Scaffold fading

**Scaffold fading** means deliberately reducing that support as learners become more capable.

The goal is not to remove help randomly. It is to transfer more of the decision-making to the learner.

### Handoff

A **handoff** is the organized transfer of work, evidence, decisions, risks, and unresolved questions to the next person, team, sprint, or course.

A good handoff says both:

- what is settled;
- what is still open, and who owns the next action.

### Provenance

**Provenance** means where something came from.

A provenance note might identify:

- the source repository;
- source file;
- source commit;
- original owner;
- whether a file is authoritative or a support copy.

### Drift

**Drift** happens when two copies that are supposed to correspond slowly stop matching.

Example: a build guide says three attempts while the authoritative manual says two.

Drift is dangerous because both copies may look reasonable in isolation.

### Stale

A file is **stale** when it was once correct but no longer reflects the current source or state.

### Superseded

**Superseded** means a newer decision or artifact has replaced an older one.

We often keep superseded material for history, but it should be clearly marked so nobody rebuilds from it accidentally.

### Retired

**Retired** means an item is intentionally no longer part of the active student path.

Retired does not necessarily mean deleted.

### Stub

A **stub** is an intentionally incomplete representation of an item because the real thing is built somewhere else.

Example: a New Quiz may have a build guide in GitHub but no HTML page file. That is not missing work; it is a different build surface.

---

## 4. Manifest, binder, render, and generated artifacts

### Manifest

A **manifest** is a structured list of what belongs in a build.

In CTS-285, the binder manifest records module order and identifies page files, build guides, hosted runtimes, stubs, optional items, and retired items.

A manifest is not merely a folder listing. It expresses **intended structure**.

### Binder

The **binder** is a generated reading/review shell that assembles course material into one place so the course can be reviewed outside Canvas.

Its purpose is inspection:

- read modules end to end;
- compare structure;
- flag problems;
- trace links and artifacts.

The binder is generated from source; it is not the source itself.

### Render

To **render** means to turn structured source into the form a person can see or use.

Examples:

- Markdown rendered as a GitHub page;
- HTML rendered by a browser;
- Canvas HTML rendered as a student page;
- manifest data rendered into the binder.

A rendering problem can exist even when the underlying source is correct.

### Generated artifact

A **generated artifact** is produced automatically from source files.

Generated artifacts should usually be reproducible: the same sources should produce the same output.

That is why we distinguish between:

- **source files we edit**;
- **generated files automation rebuilds**.

### Build ID / fingerprint

A **build ID** or **fingerprint** is a compact value derived from the inputs to a generated artifact.

If the inputs change, the fingerprint changes. That lets a tool detect that a generated file is stale.

---

## 5. Canvas and course-build vocabulary

### Canvas-ready HTML / fragment

A **Canvas-ready HTML fragment** is the body content intended to be pasted into a Canvas page.

It is a fragment rather than a complete web page: Canvas supplies the outer document, navigation, and platform shell.

### Build guide

A **build guide** tells a human how to construct something that is not represented directly by a page file.

Examples:

- a New Quiz;
- a rubric;
- an assignment configuration.

### Runtime

A **runtime** is the actual interactive experience students open and use.

In this project, hosted simulations, labs, and arcades are runtimes.

### Simulation

A **simulation** gives learners a situation in which their decisions produce consequences they can inspect.

The important feature is not animation; it is **decision → consequence → evidence**.

### Practice cabinet / arcade

These are forms of **formative practice**.

They let students make decisions and get feedback without becoming a second grading system.

### Parity

**Parity** means two implementations that are supposed to match actually match.

Examples:

- Canvas DEV ↔ source repo;
- live Canvas ↔ DEV;
- distributed starter ↔ governed starter;
- hosted runtime ↔ Canvas launch page.

### Mirror

A **mirror** is a copy maintained so another system’s current state can be inspected in the repository.

A mirror should not silently become authoritative if the project says the original system still governs.

### Retrofit

A **retrofit** updates an existing item to a newer standard without necessarily redesigning its instruction.

Examples:

- applying the current house style;
- improving accessibility structure;
- updating composition while preserving content.

### Re-paste

A **re-paste** means the source file has been corrected and the corresponding Canvas page must be updated by copying the corrected HTML back into Canvas.

### DEV

**DEV** is the development Canvas environment used to build or verify material before it reaches the live student course.

### Live

**Live** means the actual course environment used by students.

Being “in Canvas” is not automatically the same as being live or student-accessible.

---

## 6. Quality, testing, and decision vocabulary

### Requirement

A **requirement** states what a system needs to do or what constraint it must satisfy.

A concern, suggestion, or proposed solution is not automatically a requirement.

### Acceptance criterion

An **acceptance criterion** is a specific observable condition used to determine whether a requirement or story is satisfied.

### Definition of Done

A **Definition of Done** is a shared quality standard applied to completed work.

A useful Definition of Done can fail; otherwise it is a slogan, not a standard.

### Test

A **test** is executable or inspectable evidence about behavior.

Tests are especially valuable when they can detect a real failure rather than merely confirm the happy path.

### Regression

A **regression** is behavior that used to work and stops working after a change.

### Regression test

A **regression test** protects behavior that must continue to work while something else changes.

### Controlled failure

A **controlled failure** is an intentionally broken, safe practice case used to teach diagnosis.

It lets learners inspect failure without damaging their own working project.

### Verification

**Verification** asks whether the built thing behaves as specified.

Examples:

- Does the command actually run in a student Codespace?
- Does the live course match DEV?
- Does progress survive a process restart?

### Validation

**Validation** asks whether the thing being built is the right thing for the actual need.

A system can be implemented correctly and still solve the wrong problem.

### QA (Quality Assurance)

**QA** is the systematic checking of whether the implementation meets its required standards, alignment, and intended behavior.

### Gate

A **gate** is a condition that must be satisfied before dependent work should proceed.

A gate should name exactly what is blocked and what would clear it.

### Blocker

A **blocker** is something that prevents meaningful progress on dependent work.

Not every open question is a blocker.

### Closure condition

A **closure condition** states what must be true before an issue is closed.

This is especially useful for work that is intentionally waiting on:

- a course-end date;
- a human verification;
- a deployment;
- another person’s decision.

---

## 7. Team and sprint vocabulary

### Pod

A **pod** is a small working group collaborating on a shared product increment.

In CTS-285, shared work does not mean shared grades. Evidence remains individually attributable.

### Role

A **role** identifies what a person owns at greater depth during a sprint.

CTS-285 uses:

- Product Owner;
- Developer;
- Quality Lead.

### Role rotation

**Role rotation** changes who owns which responsibility so each learner experiences more than one perspective.

### Sprint

A **sprint** is a bounded period of product work focused on delivering and evaluating an increment.

### Increment

An **increment** is a meaningful addition or improvement to a working product.

### Code review

A **code review** is a structured examination of someone else’s implementation using requirements, evidence, tests, and agreed standards—not personal preference.

### Decision record

A **decision record** captures:

- the decision;
- the evidence considered;
- alternatives or constraints;
- the reason for the choice;
- unresolved risks or next actions.

A decision record makes reasoning inspectable later.

---

## 8. Common status words and what they do **not** mean

| Status | Meaning |
|---|---|
| **Proposed** | Suggested; the owner has not adopted it yet. |
| **Ratified / adopted** | The responsible owner has accepted the decision. |
| **Built** | The source/artifact exists. It may not yet be deployed. |
| **In DEV** | Present in the development environment. |
| **Live** | Present in the student delivery environment. |
| **Open to students** | Students can currently access it. |
| **Locked** | Do not change scope without an explicit reopen. |
| **Blocked** | Work is settled enough to exist but cannot proceed until a named dependency clears. |
| **Deferred** | Intentionally postponed; not forgotten. |
| **Pending verification** | Built, but still needs evidence from the real environment. |
| **Complete** | The stated closure condition is satisfied. |

These words are deliberately different. For example:

> **Built** does not mean **live**.  
> **Settled** does not mean **verified**.  
> **Open issue** does not mean **work was forgotten**.  
> **Merged PR** does not always mean **the issue can close**.

---

## 9. A practical example

Suppose a student or teammate discovers that a program forgets a first incorrect answer after the process restarts.

1. **Issue:** Record the observed problem and what behavior should persist.
2. **Branch:** Create a focused branch for the persistence repair.
3. **Evidence:** Run the existing regression tests first.
4. **Change:** Modify only the storage layer if the boundary is designed correctly.
5. **Commit:** Record the storage change.
6. **PR:** Explain the problem, boundary, evidence, and test result.
7. **Review:** A reviewer asks whether the repair changed unrelated business logic.
8. **Revision:** Adjust if needed and add evidence.
9. **Checks:** Automated tests run.
10. **Merge:** The accepted repair enters `main`.
11. **Verification:** Restart the real application and prove progress survives.
12. **Close:** Close the issue when the required behavior is verified.

The workflow leaves behind both the **working change** and the **reasoning trail**.

---

## 10. The larger idea

Version control is not only about protecting files.

Used well, GitHub becomes a record of:

- what we thought the problem was;
- what evidence changed our understanding;
- who owned the decision;
- what was tried;
- what was reviewed;
- what changed;
- what still needs verification;
- why the project looks the way it does now.

That is why issues, PRs, manifests, tests, decision records, and handoffs matter. They turn development from a pile of files into a process another person can inspect, continue, and improve.
