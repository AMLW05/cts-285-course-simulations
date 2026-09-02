# CTS 285 — Module 1 Guided Analysis Quizzes (Question Source)

Source of truth for the two guided-analysis QTI packages. Edit this file, then re-run
`python3 build_qti.py`.

These are **tutorials, not tickets**. Three attempts, feedback on every option, low
point value. They teach the workflow that the end-of-module case file assignment then
requires students to run unaided.

**Register discipline is the whole point.** Quiz A asks only about *The Story*
(Part I). Quiz B asks about *For Parents and Teachers* (Part II) and about the places
where the two parts disagree. Every answer key and every feedback string below
has been verified against `dataman-manual.md` by an independent review pass.

Features drilled here: Answer Checker, Memory Bank, Electro Flash.
Features deliberately **not** drilled, so they stay cold for the case file:
Number Guesser, Force Out, Wipe Out, Missing Number.
(Missing Number and Force Out appear in Quiz B only as reconciliation evidence,
never as features to be analyzed.)

---

## QUIZ: cts285-m1-guided-a | Guided Analysis A — Reading the Story Register

@attempts: 3
@shuffle: true
@points: 1.0

> Part I of the DataMan manual only. Answer every question using the sections under "PART I — THE STORY" in the manual transcript. Do not use the parents-and-teachers sections yet — several questions have a different correct answer there, and that difference is the subject of Guided Analysis B. Three attempts. Feedback appears on every option.

### Q1. In the Answer Checker sections of the story, which phrase most directly supports the conclusion that DataMan verifies arithmetic rather than performing it?

- [x] "you just use my keys to put in a problem you'd like to try. Then, put in your answer"
  - FB: Correct. The user supplies the answer. A system that computed the answer would not need the user to enter one. This single phrase carries the product's purpose.
- [ ] "I have keys you press to make me work"
  - FB: Incorrect. This describes the interface. It tells you how the user interacts, not what the system does with the input.
- [ ] "When I flash my lights that way, it means that you're right"
  - FB: Incorrect, though it is close. This tells you the system judges the answer, which does imply the user supplied one. But it is evidence about feedback, and the question asks which phrase supports the conclusion most directly.
- [ ] "just press my ON key"
  - FB: Incorrect. This is an operating step. It supports no conclusion about the system's purpose.

### Q2. In Answer Checker mode, what does the user supply?

- [x] Both the problem and the answer
  - FB: Correct. "put in a problem you'd like to try. Then, put in your answer." Both are user inputs. Recording only one of them would give an incomplete input list.
- [ ] Only the problem
  - FB: Incorrect. If the user supplied only the problem, DataMan would have to compute the answer. The story says the user enters the answer too.
- [ ] Only the answer
  - FB: Incorrect. The user enters the problem first. Re-read the order of operations in "Answer Checker (Story)."
- [ ] Neither — DataMan selects both
  - FB: Incorrect. DataMan selects problems in other activities, but not in Answer Checker. Do not carry a rule from one feature to another without evidence.

### Q3. According to the story, what happens after a user enters a wrong answer?

- [x] The user gets a second try, and the correct answer appears only if that try is also wrong
  - FB: Correct. "I'll give you another try. If your second try is still wrong, I'll flash EEE again, and show you the right answer!" Two tries, then reveal.
- [ ] The correct answer appears immediately
  - FB: Incorrect. That would skip the second try, which the story states explicitly.
- [ ] The problem is stored for later practice
  - FB: Incorrect. Problems are stored in the Memory Bank, and only when a person puts them there. Nothing stores wrong answers automatically.
- [ ] The user may try again as many times as needed
  - FB: Incorrect. The story caps it at two tries. An unlimited retry rule would change how the score means anything.

### Q4. The story shows this display at the end of a set of problems. What does the third number represent?

+ <div style="background:#4a72a8;color:#ffffff;font-weight:bold;font-size:22px;font-family:Georgia,serif;padding:10px 20px;display:inline-block;"><span style="padding:0 26px;">8</span><span style="padding:0 26px;">10</span><span style="padding:0 26px;">24</span></div>

- [x] The time taken, counted in ticks of DataMan's atom clock
  - FB: Correct. The story labels all three fields: number right, number of problems tried, and the time in ticks.
  - IMG: dataman-score-display.png | The labeled score display from the story section, showing number right, number tried, and time in ticks.
- [ ] The number of problems still remaining
  - FB: Incorrect. The second field already accounts for the problem count. Check the labels printed beside the figure in the manual.
- [ ] The difficulty level currently selected
  - FB: Incorrect. Difficulty is selected by pressing 1 or 2 before GO. It is not reported in the score.
- [ ] The number of tries the user needed
  - FB: Incorrect. Tries are capped at two per problem and are not totalled in the score display.

### Q5. Based only on the story sections, how long is one "tick" of DataMan's atom clock?

- [x] It cannot be determined from the story
  - FB: Correct. The story uses ticks as a unit repeatedly but never defines one. An unknown you can name is a finding, not a failure — record it.
- [ ] One second
  - FB: Incorrect. The story never says this. A familiar-sounding number is not evidence.
- [ ] One minute
  - FB: Incorrect. Nothing in the story supports any specific duration.
- [ ] It varies with the difficulty level
  - FB: Incorrect. The story makes no such claim. Part II does say the speed varies, but for a different reason — and you have not read it yet for this quiz.

### Q6. According to the story, who can put problems into the Memory Bank?

- [x] The child, a friend, or a parent
  - FB: Correct. "You, one of your friends, or Mom or Dad can put up to ten problems in my memory bank." Three distinct actors, all named.
- [ ] Only the child using the device
  - FB: Incorrect. The story names other people explicitly. Note that the person loading problems and the person answering them may be different — that distinction matters.
- [ ] Only an adult
  - FB: Incorrect. The story names the child and a friend alongside a parent.
- [ ] A parent or a teacher
  - FB: Incorrect. The story never names a teacher as someone who loads the Memory Bank. A teacher is mentioned once in Part I, but only as a pointer to the parents-and-teachers section — not as an actor. Part II does name teachers as loaders, and that difference is examined in Guided Analysis B.

### Q7. Which statement is an assumption rather than an observation, based on the story sections?

- [x] Children learn arithmetic faster with DataMan than with written worksheets
  - FB: Correct. Nothing in the story compares DataMan against any other method. A comparison needs evidence about both things being compared.
- [ ] DataMan gives the user two tries at each Memory Bank problem
  - FB: Incorrect. This is an observation. The story states it directly.
- [ ] The Memory Bank holds up to ten problems
  - FB: Incorrect. This is an observation. "up to ten problems" appears in the story.
- [ ] DataMan shows a light show after displaying a score
  - FB: Incorrect. This is an observation, stated in several story sections.

### Q8. Select every statement about Electro Flash that the story sections support. (More than one answer is correct.)

TYPE: multiple_answers

- [x] The user chooses a table by pressing a number key and one operation key
  - FB: Correct. The story states this, and adds that the two keys may be pressed in either order.
- [x] The user gets two tries at each problem
  - FB: Correct. "I'll give you two tries at each problem" appears in the story.
- [x] The score includes the number of ticks the set took to finish
  - FB: Correct. "including the number of ticks of my atom clock it took you to finish."
- [ ] The order in which the two keys are pressed changes how the problems are presented
  - FB: Not supported here. The story says only that either order is allowed. Part II adds the consequence — and that omission is a finding worth recording.
- [ ] Division tables skip any problem whose answer has a remainder
  - FB: Not supported here. This constraint appears only in Part II. Do not import it into a story-register analysis.

### Q9. Based only on the story sections, what happens if a user enters a subtraction problem whose answer would be negative?

- [x] It cannot be determined from the story
  - FB: Correct. The story never mentions negative numbers or any input the device refuses. Part II does, and the difference between what each part tells you is the point of this exercise.
- [ ] DataMan displays a negative result
  - FB: Incorrect, and unsupported. The story says nothing about negative results either way.
- [ ] DataMan displays EEE and gives a second try
  - FB: Incorrect. EEE marks a wrong answer, not a rejected input. Do not stretch one rule to cover a case the document never addresses.
- [ ] DataMan turns itself off
  - FB: Incorrect. Automatic shutoff follows about five minutes of non-use, and has nothing to do with problem content.

### Q10. Which conclusion about the Memory Bank does the story support?

- [x] A person other than the learner can decide which problems the learner practices
  - FB: Correct. Someone loads the problems, then the learner presses GO and works them. Two roles, one feature. Analysts record roles, not just users.
- [ ] Only the learner chooses which problems to practice
  - FB: Incorrect. The learner may load the Memory Bank — the story says "You . . . can put up to ten problems in my memory bank." But a friend or a parent may load it instead, so "only" is not supported.
- [ ] DataMan selects the problems automatically
  - FB: Incorrect. That describes Electro Flash. Each feature has its own source of problems — keep them separate.
- [ ] Stored problems remain in memory after the device is turned off
  - FB: Incorrect, and unsupported. The story never says what happens to stored problems at power off. Record it as an unknown.

---

## QUIZ: cts285-m1-guided-b | Guided Analysis B — Reading the Spec Register, and Reconciling the Two

@attempts: 3
@shuffle: true
@points: 1.0

> Part II of the DataMan manual — "For Parents and Teachers" — plus the places where Part I and Part II disagree. You will need both parts open. Several questions ask you to decide whether a difference between the two is a real conflict or only an apparent one. Three attempts. Feedback appears on every option.

### Q1. What input limits does "Answer Checker (Operating Notes)" state?

- [x] Problems may use one or two digit numbers; answers may be one, two, or three digits
  - FB: Correct. Note that the limits differ for problems and answers. Recording a single "1-3 digits" rule would lose a real constraint.
- [ ] Both problems and answers are limited to two digits
  - FB: Incorrect. Answers may be three digits — necessary, since two two-digit numbers can multiply past 99.
- [ ] Problems and answers may both be up to three digits
  - FB: Incorrect. Problems are capped at two digits. Re-read the sentence beginning "DataMan will only accept."
- [ ] The manual states no limit on either
  - FB: Incorrect. The limits are stated plainly. This is exactly the kind of constraint the story register omits entirely.

### Q2. The operating notes trace what happens when a user presses 7, −, 8, =. What does DataMan do?

- [x] It refuses the 8, and the display stops at "7 −"
  - FB: Correct. The device rejects the keystroke that would produce a negative result. The invalid input is never accepted, so no error state is needed.
- [ ] It accepts the entry and displays a negative result
  - FB: Incorrect. The manual states DataMan is not built to handle negative numbers.
- [ ] It accepts the entry and displays EEE
  - FB: Incorrect. EEE marks a wrong *answer*. This is a rejected *input* — a different mechanism, and worth recording separately.
- [ ] It clears the display and returns to Answer Checker
  - FB: Incorrect. The 7 and the minus sign remain. The user may continue by entering a number of 7 or less.

### Q3. The story says the Missing Number box "keeps moving from the left to the right of the problem." The operating notes say the first press puts the box at the right, the second at the left, and the third in the middle. What should an analyst record?

- [x] A conflict between the two sections, which must be resolved before the requirement can be trusted
  - FB: Correct — and there is a further wrinkle worth finding. The story's own worked examples run right, left, middle, matching the operating notes. So the story's prose disagrees with the operating notes *and* with the story's own examples. Naming the conflict is the finding; resolving it needs the device or a subject-matter expert.
- [ ] The operating notes are correct, because technical sections are authoritative
  - FB: Incorrect. Nothing establishes one section as authoritative. Elsewhere in this manual the story carries requirements the operating notes omit entirely.
- [ ] The story is correct, because it describes what the user sees
  - FB: Incorrect. Both sections describe what the user sees. Audience does not settle accuracy.
- [ ] The two statements agree
  - FB: Incorrect, though you may have noticed something real. The story's *examples* do match the operating notes. Its prose sentence does not. A document that disagrees with itself still has a conflict to record.

### Q4. Both parts say the Electro Flash number key and operation key may be pressed in either order. What does the operating notes section add that the story leaves out?

- [x] The order determines the order in which the numbers appear in the problem
  - FB: Correct. The story says the choice is free; the operating notes say the choice has a consequence. A reader of the story alone would conclude the order does not matter.
- [ ] That the user must press GO to begin
  - FB: Incorrect. Both sections state this.
- [ ] That the user gets two tries at each problem
  - FB: Incorrect — the story already states this, so the operating notes do not add it. Worth noticing, though: the Electro Flash operating notes never mention the two-try rule at all. Here the story is the more complete source.
- [ ] That a light show follows the score
  - FB: Incorrect. Both sections state this.

### Q5. The story shows Force Out starting at 37. The operating notes show it starting at 63. What should an analyst conclude?

- [x] There is no conflict — the operating notes state the starting number differs each time
  - FB: Correct. "DataMan will display a number (a different one each time)." The two figures are examples of a varying value. Not every difference is a defect.
- [ ] The two sections conflict and must be reconciled
  - FB: Incorrect. Check whether the document explains the difference before recording it as a conflict. Here it does.
- [ ] The story is out of date
  - FB: Incorrect. Nothing indicates either section is older. The difference has a stated cause.
- [ ] Force Out always begins at 63
  - FB: Incorrect. This is the error the "different one each time" sentence exists to prevent.

### Q6. According to the manual, how many seconds is one tick of DataMan's atom clock?

- [x] It cannot be determined — the manual states the clock speed varies
  - FB: Correct. "The actual speed of his clock may vary depending on how fresh the battery is, room temperature, etc." The document declares the value indeterminate, which is itself a firm finding.
- [ ] One second
  - FB: Incorrect. No fixed duration is given anywhere in the manual.
- [ ] It is stated in the Appendix
  - FB: Incorrect. The Appendix covers battery, error indications, and service. It does not define the tick.
- [ ] It varies by activity
  - FB: Incorrect. The stated causes are battery freshness and room temperature, not which activity is running.

### Q7. Select every item that appears in the operating notes but **not** in the story. (More than one answer is correct.)

TYPE: multiple_answers

- [x] The digit limits on problems and answers
  - FB: Correct. Stated only in "Answer Checker (Operating Notes)."
- [x] The refusal of subtraction that would produce a negative answer
  - FB: Correct. The story never mentions negative numbers at all.
- [x] That division tables skip problems whose answers have remainders
  - FB: Correct. This appears in the Electro Flash operating notes only.
- [ ] That the user gets two tries at each problem
  - FB: This appears in both parts, so it does not belong in a spec-only list.
- [ ] That a light show follows the score
  - FB: This appears in both parts.

### Q8. Which detail about Wipe Out appears in the story but **not** in the operating notes?

- [x] After two misses, DataMan answers the problem for the player
  - FB: Correct. The story states it; the operating notes are silent. The story register is not merely decorative — it carries requirements found nowhere else.
- [ ] The time until wipe out is chosen at random
  - FB: Incorrect, but read the two statements closely — they are not the same claim. The story says only that the time is secret: "Only I know when time will run out." The operating notes say it is "selected at random." Secrecy and randomness are different properties, and only one of them is stated in the story.
- [ ] The game is for two or more players
  - FB: Incorrect. Both parts describe it as a multi-player game.
- [ ] The problems presented are addition problems
  - FB: Incorrect — and reversed. That detail is in the operating notes only.

### Q9. Comparing how each part describes who loads the Memory Bank, what does the operating notes section add?

- [x] Teachers, whom the story never names as people who load the Memory Bank
  - FB: Correct. The story names the child, a friend, and a parent. The operating notes name parents, teachers, or friends. Notice also what the operating notes drop: the child, whom the story lists first. Neither actor list is complete.
- [ ] Friends, who are never named in the story
  - FB: Incorrect. The story names friends explicitly.
- [ ] Parents, who are never named in the story
  - FB: Incorrect. The story names "Mom or Dad."
- [ ] Nothing — both sections name the same people
  - FB: Incorrect. Compare the two lists item by item. One name appears in only one of them.

### Q10. The Memory Bank and Missing Number score displays report three numbers, the third being elapsed time. The Answer Checker score reports only two, with no time. Which explanation does the manual support?

- [x] The timer starts when GO is pressed, and Answer Checker does not use GO
  - FB: Correct, and this is the kind of finding that makes an analyst useful. No sentence states it outright. You assemble it: the Memory Bank notes say "You then press GO to make the problems reappear one at a time and to start DataMan's built-in timer," and nothing in Answer Checker involves GO. Evidence from two places, combined.
  - IMG: dataman-keypad.png | The DataMan keypad as illustrated in the manual. GO sits at the lower left of the number pad.
- [ ] Answer Checker problems are not timed because they are easier
  - FB: Incorrect. The manual never rates Answer Checker as easier, and difficulty is not what starts or stops the timer.
- [ ] The manual omits the Answer Checker time by mistake
  - FB: Incorrect. Both Answer Checker descriptions agree on two fields, in both registers. Consistent across two registers is weak evidence for an error.
- [ ] DataMan has no timer hardware, and the times shown are estimates
  - FB: Incorrect. "DataMan's Timer" describes a built-in timer and a moving light display. Nothing suggests the values are estimated.

### Q11. Having read both parts, which conclusion about this manual is best supported?

- [x] Neither part is complete on its own, so conclusions require checking both
  - FB: Correct. Each part carries requirements the other omits, and at least one point where they disagree. This is normal for real documentation, and it is why analysts triangulate rather than trust a single source.
- [ ] The operating notes supersede the story wherever they differ
  - FB: Incorrect. The Wipe Out two-miss rule and the difficulty-level toggle appear only in the story. Supersession would discard real requirements.
- [ ] The story is written for children and carries no requirements
  - FB: Incorrect. Several behaviors are documented only in the story. Audience does not determine whether text carries requirements.
- [ ] The manual is internally consistent
  - FB: Incorrect. The Missing Number box travel is described two incompatible ways.
