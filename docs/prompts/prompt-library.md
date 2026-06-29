# CareBridge Reusable Prompt Library

A copy-paste library of every prompt used across the [AI-Powered Agile artifacts](../agile-ai/README.md), generalized so you can drop them into your own projects. Replace anything in `{curly braces}` with your specifics. Every prompt uses the structured template explained in the [prompt engineering guide](../agile-ai/00-prompt-engineering-guide.md):

```text
#ROLE  ·  #TASK  ·  #AUDIENCE  ·  #FORMAT  ·  #SUCCESS METRICS
```

**How to use this file:** find the situation you're in, copy the fenced block, fill the `{variables}`, run it : then apply your own judgment to the draft. AI drafts; you decide and own the outcome.

---

## Chapter 1 : Managing projects

### 1.1 Prioritize a product backlog
*Use when you have a flat list of backlog items and need a defensible, outcome-driven order.*

```text
#ROLE      Experienced Product Owner for {product / domain, e.g. a regulated
           digital-health platform}.
#TASK      Rank the following backlog items for {milestone, e.g. a pilot-ready
           MVP}. Score each on impact toward {primary outcome, e.g. cutting
           avoidable 30-day readmissions} and on delivery effort. Flag any item
           that is a {hard constraint, e.g. HIPAA/audit-trail} prerequisite that
           must ship first regardless of score.
           Items: {paste backlog items}.
#AUDIENCE  {who consumes this, e.g. the delivery team and exec sponsor}.
#FORMAT    A table: Item | Impact (H/M/L) | Effort (H/M/L) | Priority | Rationale.
#SUCCESS METRICS  Sequencing that delivers {goal, e.g. a pilot-ready MVP in
           2 quarters for 3 health systems} with {must-haves} in early releases.
```

### 1.3 Refine fuzzy requirements
*Use during backlog refinement when a story or requirement feels vague or risky to estimate.*

```text
#ROLE      Senior Business Analyst on {product / domain}.
#TASK      Analyze the following requirement(s) for ambiguity, missing
           acceptance criteria, and gaps. Identify what is unspecified
           (including any {compliance/PHI/security} implications) and rewrite
           each as an INVEST-quality user story.
           Requirement(s): {paste stories/requirements}.
#AUDIENCE  The delivery team during refinement.
#FORMAT    Two sections : (1) bulleted gap analysis, (2) rewritten stories with
           acceptance criteria.
#SUCCESS METRICS  Stories the team can estimate and build without follow-up
           questions, satisfying {key constraint, e.g. audit-trail logging}.
```

### 1.4 Summarize a sprint retrospective
*Use after a retro to turn raw notes into a shareable summary with owned actions.*

```text
#ROLE      Experienced Scrum Master facilitating a {team type} team's retro.
#TASK      Summarize the following retrospective notes. Group into What went
           well / What didn't / Action items. For each action, propose an owner
           and a measurable check.
           Notes: {paste raw retro notes}.
#AUDIENCE  The {N}-person delivery team and the PM.
#FORMAT    Three bulleted sections, then an action table:
           Action | Owner | Check | Due sprint.
#SUCCESS METRICS  At most {N} high-leverage actions that improve {flow metric,
           e.g. WIP, cycle time, or audit-trail coverage} next sprint.
```

---

## Chapter 2 : Building the team

### 2.1 Scope an Agile delivery team
*Use before opening requisitions to pressure-test which roles you truly need.*

```text
#ROLE      Highly experienced Scrum Master with a track record of shipping
           {domain, e.g. regulated healthcare} software.
#TASK      Put an Agile delivery team together to ship {outcome and horizon,
           e.g. a pilot-ready MVP within 2 quarters}. First list the
           considerations and roles I should weigh. Then produce the team in a
           table: team member | skillset | capabilities. Then do a second
           iteration that combines any roles that one person could credibly
           carry, for a leaner pilot squad.
#AUDIENCE  The PM staffing the team.
#FORMAT    (1) bulleted considerations, (2) full-team table, (3) combined-role
           table.
#SUCCESS METRICS  A team that can take a vertical slice from idea to done at a
           {cadence, e.g. 2-week} cadence and clear {constraint, e.g. a
           HIPAA-conscious} bar.
```

### 2.1 Write a job description
*Use to draft a requisition for a specific delivery role.*

```text
#ROLE      Experienced HR Professional partnering with engineering leadership.
#TASK      Write a job description for a {role, e.g. Backend Engineer} who will
           {core responsibility, e.g. build the API and HIPAA-style audit trail}
           on {product}. Cover summary, responsibilities, required and preferred
           skills, and what success looks like in the first 90 days.
#AUDIENCE  Qualified candidates and the hiring panel.
#FORMAT    A structured job posting with clear headings and bullet points.
#SUCCESS METRICS  A posting that attracts candidates who can deliver against
           {project goal} and pass a {constraint, e.g. security-conscious} bar.
```

### 2.2 Assess team Agile knowledge
*Use to baseline a team's Agile understanding before coaching or onboarding.*

```text
#ROLE      Agile Coach assessing a {team type} team.
#TASK      Generate a {N}-question quiz that measures practical understanding of
           {topics, e.g. Scrum roles, ceremonies, backlog refinement, DoD}.
           Mix recall and applied-scenario questions. Provide an answer key with
           one-line explanations.
#AUDIENCE  The delivery team (self-assessment) and the Scrum Master.
#FORMAT    Numbered questions, then a separate answer key.
#SUCCESS METRICS  Results that reveal real coaching gaps, not just trivia recall.
```

### 2.2 Build a SCRUM × SCARF matrix
*Use to plan change adoption : mapping ceremonies to the brain's social drivers.*

```text
#ROLE      Agile Coach fluent in the SCARF model (Status, Certainty, Autonomy,
           Relatedness, Fairness).
#TASK      Map our SCRUM ceremonies/practices against the five SCARF dimensions.
           For each cell, note how the practice can threaten or reward that
           driver, and a facilitation tip to keep it a reward.
           Practices: {list ceremonies, e.g. planning, daily, review, retro}.
#AUDIENCE  The Scrum Master and team leads.
#FORMAT    A matrix: rows = SCRUM practices, columns = the five SCARF dimensions.
#SUCCESS METRICS  Concrete facilitation moves that reduce change resistance in
           a {team type} team.
```

### 2.3 Plan onboarding with the 5Es framework
*Use to design a structured ramp for new or cross-functional team members.*

```text
#ROLE      Agile Coach designing onboarding for {product}'s delivery team.
#TASK      Build a {duration, e.g. 2-week} cross-functional onboarding plan
           using the 5Es framework (Engage, Explore, Explain, Elaborate,
           Evaluate). For each E, give activities, owners, and an exit check.
#AUDIENCE  New joiners across {roles}.
#FORMAT    A table per E, or one table: Phase (E) | Activities | Owner | Exit check.
#SUCCESS METRICS  A new member contributing a {first deliverable, e.g. vertical
           slice} by end of the plan.
```

---

## Chapter 3 : Culture & regulation

### 3.1 Diagnose culture inhibitors (Agile Culture Matrix)
*Use to surface what's blocking an Agile transformation and where each blocker sits.*

```text
#ROLE      Agile Coach diagnosing organizational culture.
#TASK      Identify the cultural inhibitors blocking Agile adoption at
           {organization/context}. Place each on an Agile Culture Matrix
           ({axes, e.g. behavior vs. mindset, or individual vs. systemic}) and
           recommend an intervention for each.
#AUDIENCE  Leadership sponsoring the transformation.
#FORMAT    A matrix plus an inhibitor → intervention table.
#SUCCESS METRICS  A short, prioritized set of interventions leadership can own.
```

### 3.2 Design a culture/enablement program
*Use to turn culture goals into a concrete education and leadership program.*

```text
#ROLE      Agile Coach and servant-leadership practitioner.
#TASK      Design a culture program for {context} combining (1) an education
           track, (2) servant-leadership practices for managers, and (3) a
           collaboration survey to baseline and track team health.
#AUDIENCE  Managers and the delivery team(s).
#FORMAT    Program outline + a ready-to-send collaboration survey (questions +
           scale).
#SUCCESS METRICS  Measurable improvement in {collaboration/health metric} over
           {timeframe}.
```

### 3.3 Build a regulatory register
*Use to enumerate and track compliance obligations for a regulated product.*

```text
#ROLE      Cybersecurity Analyst experienced in {regulations, e.g. HIPAA and
           GDPR} for {data type, e.g. health data}.
#TASK      Identify the regulatory obligations {product} must satisfy across
           {jurisdictions}. For each, diagnose current exposure given
           {current state, e.g. a JWT-auth stub and READ/WRITE audit log}.
#AUDIENCE  The PM and {customer} compliance officers.
#FORMAT    A register: Regulation | Jurisdiction | Obligation | Current state |
           Gap | Owner.
#SUCCESS METRICS  A register defensible in a customer security review and
           supporting {readiness goal, e.g. HIPAA + SOC 2 Type II before GA}.
```

### 3.4 Build a multi-geography risk register
*Use when expanding a product into new countries/markets.*

```text
#ROLE      Project Manager experienced in multi-geography {domain} delivery.
#TASK      Build a risk register for expanding {product} into {geographies, e.g.
           the US, Germany (EU), and Canada}. Cover regulatory, data-residency,
           operational, and clinical/safety risks. Score and propose mitigations.
#AUDIENCE  The exec sponsor and pilot stakeholders.
#FORMAT    A register: Risk | Geography | Likelihood | Impact | Mitigation | Owner.
#SUCCESS METRICS  A prioritized, owned set of risks that protects {goal, e.g.
           a HIPAA-conscious multi-region pilot}.
```

---

_Source technique: AI-Powered Agile workbook (Chapters 1–3). For the technique itself, see the [prompt engineering guide](../agile-ai/00-prompt-engineering-guide.md)._
