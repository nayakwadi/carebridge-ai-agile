# Prompt Engineering for AI-Powered Agile

*Course mapping — Workbook "ChatGPT Cheat Sheet": the prompt technique that underpins every artifact in this folder.*

Every artifact under `docs/agile-ai/` is produced with one repeatable prompting discipline. This guide is the technique itself — the pattern, the vocabulary, the richer template I use in practice, and the human-in-the-loop guardrail that keeps me (the PM) accountable for the result.

## The core pattern

The workbook's "ChatGPT Cheat Sheet" reduces a good prompt to three moves:

> **Act as a `<ROLE>` → Create a `<TASK>` → Show as a `<FORMAT>`**

You tell the model *who to be*, *what to do*, and *how to hand it back*. That single sentence already outperforms the vague "help me with my backlog" prompt, because it removes ambiguity on all three axes at once. A worked instance:

> *Act as a **Product Owner**. **Rank** this CareBridge backlog by readmission-reduction impact and effort. Show it as a **Table**.*

### The cheat-sheet vocabulary

The workbook suggests starter lists for each slot. Mix and match — pick one ROLE, one or more TASK verbs, one FORMAT.

| ROLE (Act as a…) | TASK (Create a…) | FORMAT (Show as a…) |
|---|---|---|
| Scrum Master | Generate | Table |
| Product Owner | Summarize | PDF |
| Developer | Analyze | Plain Text |
| Scrum Team Member | Identify | PowerPoint |
| Agile Coach | Validate | Excel |
| Skilled Software Developer | Personalize | List |
| Qualified Engineer | Diagnose | Summary |
| Trusted Consultant | Rank | Bullet Points |
| Project Manager | Improve | Rich Text |
| Cybersecurity Analyst | Design | CSV File |
| Business Analyst | Enhance | Survey |
| UX Designer | Monitor | |
| HR Professional | Customize | |

**How to read it:** the ROLE sets the model's expertise and voice (a *Cybersecurity Analyst* will surface threat surfaces a *UX Designer* never would). The TASK verb sets the cognitive operation (*Diagnose* and *Rank* produce very different outputs from the same data). The FORMAT decides whether the answer drops straight into a Jira table, a stakeholder deck, or a `.csv` import. Choosing deliberately across all three is the whole skill.

## The richer structured template I actually use

The three-move pattern is the floor, not the ceiling. Across this portfolio I use a fuller, labeled template that makes the prompt auditable and repeatable — the same way I'd write an acceptance criterion. It adds **audience** and **success metrics** so the model optimizes for the right reader and the right outcome:

```text
#ROLE      Who the model should be — its expertise and point of view.
#TASK      The specific operation, with enough context to be unambiguous.
#AUDIENCE  Who will consume the output — sets tone, depth, and jargon level.
#FORMAT    The exact shape of the deliverable (table, list, register, survey…).
#SUCCESS METRICS  What "good" looks like — the bar the output must clear.
```

- **#ROLE** — Borrowed straight from the cheat-sheet ROLE column. It primes domain knowledge and tone. "Act as an experienced Scrum Master with a reputation for shipping regulated healthcare software" beats a bare "Scrum Master."
- **#TASK** — The cheat-sheet TASK verb plus the concrete object and constraints. Vague tasks get vague answers; "Analyze these 8 backlog items for ambiguity and missing acceptance criteria" is testable.
- **#AUDIENCE** — Who reads this: the delivery team, a pilot hospital's compliance officer, an exec sponsor? The model calibrates depth and language to the reader.
- **#FORMAT** — The cheat-sheet FORMAT column. Demanding a table, a register, or a CSV up front saves a reformatting round-trip and makes outputs comparable across sprints.
- **#SUCCESS METRICS** — The PM-grade addition. I anchor these to CareBridge's OKRs (15% readmission reduction across 3 pilot systems in 12 months; ≥90% care-task completion; HIPAA + SOC 2 Type II readiness before GA) so the model is reasoning toward outcomes, not just producing text.

## Worked CareBridge examples

### Example 1 — Prioritizing the backlog

**Weak prompt**

```text
Help me prioritize my backlog.
```

This gives the model no role, no ranking criteria, no audience, and no format. It will guess — usually returning a generic, unprioritizable list.

**Strong structured prompt**

```text
#ROLE      Experienced Product Owner for a regulated US digital-health product.
#TASK      Rank these 10 CareBridge backlog items for our pilot-ready MVP.
           Score each on impact toward cutting avoidable 30-day readmissions
           and on delivery effort. Flag any item that is a HIPAA/audit-trail
           prerequisite and must ship first regardless of score.
#AUDIENCE  The CareBridge delivery team and the exec sponsor.
#FORMAT    A table: Item | Impact (H/M/L) | Effort (H/M/L) | Priority | Rationale.
#SUCCESS METRICS  Sequencing that lands a pilot-ready MVP in 2 quarters for
           3 health systems, with the auditable trail in the first releases.
```

### Example 2 — Refining a fuzzy requirement

**Weak prompt**

```text
Is this user story good?
"As a nurse I want to see patients."
```

**Strong structured prompt**

```text
#ROLE      Senior Business Analyst on a HIPAA-conscious care-coordination platform.
#TASK      Analyze this user story for ambiguity, missing acceptance criteria,
           and gaps. The story: "As a nurse I want to see patients."
           Identify what's unspecified (which patients, what fields, what
           filtering, what audit/PHI-access implications) and rewrite it.
#AUDIENCE  The delivery team during backlog refinement.
#FORMAT    Two sections — (1) a bulleted gap analysis, (2) a rewritten story
           with INVEST-quality acceptance criteria.
#SUCCESS METRICS  A story a Frontend and Backend engineer could estimate and
           build without follow-up questions, with PHI access logged to the
           audit trail.
```

### Example 3 — Diagnosing a regulatory blind spot

**Weak prompt**

```text
What compliance stuff do we need?
```

**Strong structured prompt**

```text
#ROLE      Cybersecurity Analyst experienced in HIPAA and GDPR for health data.
#TASK      Identify the regulatory obligations CareBridge must satisfy as we
           expand from the US into Germany (EU) and Canada. For each, diagnose
           our current exposure given a JWT-auth stub and READ/WRITE audit log.
#AUDIENCE  The PM and the pilot health systems' compliance officers.
#FORMAT    A regulatory register table: Regulation | Jurisdiction | Obligation |
           Current state | Gap | Owner.
#SUCCESS METRICS  A register that supports HIPAA + SOC 2 Type II readiness
           before GA and is defensible in a customer security review.
```

In all three, the strong prompt is not longer for its own sake — every line removes a decision the model would otherwise make for me, badly.

## Human-in-the-loop: the AI drafts, the PM owns

The technique above makes AI a fast, tireless *drafting partner* — nothing more. **AI generates the first draft; I verify it, decide what to keep, change, or challenge, and I own the outcome.** Every artifact in this folder closes with a "PM judgment applied" section for exactly this reason: it records where I overrode the model (e.g., refusing to fold the Clinical SME into another role, or splitting a Product-Owner/Scrum-Master merge). The model has no accountability for a missed readmission target or a HIPAA finding — I do. Use the prompts to move faster, never to outsource the judgment.

_Reusable prompts: [prompt-library](../prompts/prompt-library.md) · Source technique: AI-Powered Agile workbook, "ChatGPT Cheat Sheet."_
