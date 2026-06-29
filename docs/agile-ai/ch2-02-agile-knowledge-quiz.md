# Agile Knowledge Quiz for the CareBridge Team

*Course mapping — Workbook §2.2: Using AI to assess and level-set a team's Agile knowledge*

## Scenario

The CareBridge delivery team is cross-functional and newly formed — some members are deep in Scrum, others (notably the Clinical SME) are new to Agile ceremonies. Before our first sprint I used AI to generate a short, fair knowledge check so I could spot gaps and tailor coaching, rather than assume everyone shares the same vocabulary.

## The prompt I used

```text
You are a highly experienced agile coach who onboards cross-functional teams.
Put together 10 multiple choice questions to assess the team's Agile knowledge.
Cover Scrum events, roles, the product backlog, estimation, retrospectives,
WIP limits, and the Definition of Done. Each question should have four options
(A–D). Highlight the correct answers in bold. Tie a couple of the questions to
our context: CareBridge, a HIPAA-conscious healthcare platform built by a
cross-functional squad running 2-week sprints.
```

## AI-generated output

**1. How long is the CareBridge team's sprint (iteration)?**
A. 1 week
**B. 2 weeks**
C. 30 days
D. However long the story takes

**2. Who is accountable for ordering and maximizing the value of the Product Backlog?**
A. The Scrum Master
**B. The Product Owner**
C. The whole development team by vote
D. The most senior engineer

**3. What is the primary purpose of the Daily Scrum?**
A. To report status up to management
**B. To inspect progress toward the Sprint Goal and adapt the plan for the next day**
C. To assign tasks to each developer
D. To run detailed design discussions

**4. The CareBridge team agrees that "done" includes passing automated tests AND verifying that every PHI access is captured in the audit log. This shared agreement is the team's:**
A. Sprint Goal
B. Acceptance criteria for one story
**C. Definition of Done**
D. Product Backlog item

**5. What does a Work-In-Progress (WIP) limit on the care-plan Kanban board do?**
A. Caps how many stories can be in the whole sprint
**B. Caps how many items can be in a workflow stage at once, to expose bottlenecks and improve flow**
C. Limits how many people can work on the team
D. Sets the maximum story-point total per sprint

**6. Which statement best describes a Sprint Retrospective?**
A. The team demos completed work to stakeholders
**B. The team inspects how it worked and commits to specific improvements for the next sprint**
C. The Product Owner re-prioritizes the backlog
D. The Scrum Master reviews individual performance

**7. The team estimates backlog items in story points. Story points primarily express:**
A. The exact number of hours a task will take
**B. Relative size — effort, complexity, and uncertainty combined**
C. The business priority of an item
D. The number of developers needed

**8. During Sprint Review for CareBridge, the Clinical SME flags that the new care-plan flow doesn't match a real hospital-to-home handoff. What should happen?**
A. Ship it anyway; it's already coded
B. Ignore it until after GA
**C. Capture the feedback and let the Product Owner adjust the Product Backlog accordingly**
D. Open a change request and skip the next review

**9. Who is responsible for removing impediments and protecting the team's focus?**
A. The Product Owner
**B. The Scrum Master**
C. The DevOps/SRE engineer
D. Whoever raised the blocker

**10. What is the main purpose of Backlog Refinement (grooming)?**
A. To assign every backlog item to a developer
B. To estimate the team's salaries
**C. To add detail, estimates, and order to backlog items so they're ready for upcoming sprints**
D. To close the current sprint

**Scoring guide:** 9–10 = strong Agile fluency; 6–8 = solid, target the missed areas in coaching; ≤5 = pair with the Scrum Master for a working-agreements refresher before Sprint 1.

## PM judgment applied

- **Kept the two CareBridge-specific items (Q4, Q8) front and center.** AI's first pass was generic Scrum trivia; I pushed for questions tied to our audit-trail Definition of Done and a real care-transition workflow, which makes the assessment relevant and surfaces clinical-Agile gaps.
- **Verified each "correct" answer against the Scrum Guide.** I checked the Daily Scrum, retrospective, and PO-accountability answers for accuracy rather than trusting the bolding — AI occasionally mislabels the team-accountability questions.
- **Cut a duplicate question.** AI produced two near-identical WIP-limit items; I removed one and replaced it with the Backlog Refinement question (Q10) to widen coverage.
- **Added the scoring guide as a coaching tool, not a grade.** I reframed results toward targeted coaching so the quiz builds the team up instead of ranking individuals.

_Reusable prompt: [prompt-library](../prompts/prompt-library.md) · Source technique: AI-Powered Agile workbook §2.2._
