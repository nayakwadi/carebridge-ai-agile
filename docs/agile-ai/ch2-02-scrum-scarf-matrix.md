# SCRUM × SCARF Matrix for the CareBridge Team

*Course mapping — Workbook §2.2: Combining the SCRUM framework with the SCARF model to shape ways of working*

## Scenario

The CareBridge squad is a mix of clinical and engineering minds working under real compliance pressure. Strong ceremonies aren't enough — people show up safe and engaged only when their social-brain needs are met. I used AI to cross-reference our **SCRUM** events with David Rock's **SCARF** model so our ways of working actively reduce threat and increase engagement, especially for the Clinical SME who is new to Agile.

## The prompt I used

```text
#ROLE
Act as an experienced SCRUM master with 15 years' experience coaching
cross-functional teams in regulated environments.

#TASK
Cross reference both SCRUM and SCARF, put them together and suggest ways,
activities and considerations for my team's ways of working. Briefly explain
SCARF first.

#AUDIENCE
A cross-functional CareBridge team — clinical SME, engineering, scrum master —
building a HIPAA-conscious patient care-coordination platform in 2-week sprints.

#FORMAT
A matrix that cross references both frameworks and includes concrete activities
that support the overlap. Rows = SCRUM events/practices; columns = the 5 SCARF
domains.
```

## AI-generated output

### SCARF in brief

David Rock's **SCARF** model names five social domains that the brain treats like survival needs. When they're threatened, people disengage; when they're rewarded, people collaborate:

- **Status** — sense of relative importance and being valued.
- **Certainty** — ability to predict what's coming.
- **Autonomy** — a sense of control and choice over one's work.
- **Relatedness** — feeling of safety and belonging with others.
- **Fairness** — perception that exchanges and decisions are just.

### Matrix — SCRUM events × SCARF domains

| SCRUM practice | Status | Certainty | Autonomy | Relatedness | Fairness |
|---|---|---|---|---|---|
| **Sprint Planning** | Let each discipline (clinical, FE, BE, data, QA) present and own its slice, so expertise is visibly valued | Set a clear Sprint Goal and capacity so everyone can predict the 2 weeks ahead | Let the team pull and self-assign work rather than the PO dictating tasks | Plan as one group; include the Clinical SME so clinical and technical views meet early | Use transparent capacity and a shared estimation method (story points) so load is seen as fair |
| **Daily Scrum** | Give equal airtime; no one's update is "more senior" | Reaffirm the Sprint Goal daily so progress stays predictable | Let people frame their own plan for the day, not receive assignments | Keep it human and brief; a quick personal check-in builds belonging | Apply the same 3-question format to every member, every day |
| **Backlog Refinement** | Credit the Clinical SME for domain insight that reshapes a story | Add acceptance criteria and the audit-trail Definition of Done so items are unambiguous | Let the team challenge and split stories, not just receive them | Refine collaboratively across clinical + engineering, surfacing dependencies together | Order the backlog by transparent value/risk criteria, openly discussed |
| **Sprint Review** | Have the people who built each feature demo it — public credit for the work | Show a working increment so stakeholders and team see concrete, certain progress | Let the team decide how to demo and what to highlight | Invite the 3 pilot stakeholders and the Clinical SME into one shared conversation | Tie feedback to the agreed Sprint Goal, not shifting personal opinions |
| **Sprint Retrospective** | Value every voice equally; quietest members speak first | Close with a small number of concrete, agreed improvements so next sprint feels safer | Let the team choose its own experiments and working agreements | Use a psychologically safe format (e.g. start/stop/continue) that builds trust | Address process problems and decisions, never blame individuals |

## PM judgment applied

- **Kept the explicit Clinical-SME cues in every row.** AI gave a generic matrix; I had it call out where our nurse-informaticist's status, certainty, and relatedness are most at risk as the only non-engineer, since that's exactly where this team will fracture if I'm not deliberate.
- **Challenged "Status" framing toward credit, not hierarchy.** AI's draft leaned on seniority; I reframed Status around visible credit for expertise and equal airtime, which fits a flat, cross-functional squad far better.
- **Verified the Fairness column ties to our real artifacts.** I anchored Fairness to transparent estimation, the shared audit-trail Definition of Done, and open backlog ordering — concrete CareBridge practices rather than vague "be fair" advice.
- **Added the audit-trail DoD into Certainty and Refinement cells.** Because ambiguity around compliance is a real anxiety source here, I made our Definition of Done an explicit certainty lever.

_Reusable prompt: [prompt-library](../prompts/prompt-library.md) · Source technique: AI-Powered Agile workbook §2.2._
