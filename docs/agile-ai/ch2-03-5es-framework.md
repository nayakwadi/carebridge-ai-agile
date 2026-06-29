# 5Es Framework for Cross-Functional Collaboration

*Course mapping — Workbook §2.3: Applying the 5Es framework to structure a cross-functional sprint*

## Scenario

A formed team isn't a collaborating team. For the CareBridge squad's first real sprint, I wanted a deliberate structure for how clinical and engineering members engage, learn, and improve together over two weeks — not just a stack of ceremonies. I used AI to map the **5Es framework** (Engage, Educate, Enable, Empower, Evaluate) onto our 2-week sprint timeline.

## The prompt I used

```text
#ROLE
Act as an experienced SCRUM master with 15 years experience facilitating
cross-functional teams.

#TASK
Apply the 5Es framework for cross-team collaboration. Use the 5Es framework
(Engage, Educate, Enable, Empower, Evaluate) to showcase how my team can
structure and facilitate their work processes across a single 2-week sprint.

#AUDIENCE
A cross-functional CareBridge team — HR/clinical SME, engineering, scrum master —
building a HIPAA-conscious patient care-coordination platform.

#FORMAT
A table: one side lists the 5Es activities, the other side a timeline spread
across 2 weeks (by day/week).
```

## AI-generated output

### The 5Es, defined

- **Engage** — get everyone aligned, included, and bought into the goal.
- **Educate** — share the context, domain knowledge, and standards people need.
- **Enable** — remove friction; give the team the tools, access, and clarity to do the work. *(also "Equip")*
- **Empower** — hand the team autonomy and authority to make decisions and own outcomes.
- **Evaluate** — inspect results and the way of working, then adapt.

### 2-week sprint mapped to the 5Es

| 5E phase | Activities for the CareBridge team | When (2-week sprint) |
|---|---|---|
| **Engage** | Sprint Planning: agree the Sprint Goal; Clinical SME frames the target care-transition workflow; everyone pulls and owns a slice of the vertical (UI → API → data → audit) | **Week 1 · Day 1** |
| **Educate** | Clinical SME walks the team through the real hospital→home→specialist handoff and PHI/audit constraints; Backend Engineer briefs the team on the audit-logging Definition of Done | **Week 1 · Day 1–2** |
| **Enable** | DevOps confirms environments, Docker Compose, and repo access are ready; Data Engineer ensures seed data and migrations are in place so no one is blocked building care-plan and task features | **Week 1 · Day 2–3** |
| **Empower** | Team self-organizes around the board with WIP limits; engineers and Clinical SME make scoping calls within the Sprint Goal; daily check-ins surface blockers fast — the Scrum Master clears, doesn't direct | **Week 1 · Day 3 → Week 2 · Day 8** |
| **Evaluate (mid-sprint)** | Lightweight mid-sprint sync: verify the audit trail captures READ/WRITE correctly; re-confirm the increment matches the clinical workflow before it hardens | **Week 2 · Day 6 (mid-point)** |
| **Evaluate (Review)** | Sprint Review: demo the working increment to the 3 pilot stakeholders and Clinical SME; capture feedback into the backlog | **Week 2 · Day 9** |
| **Evaluate (Retro)** | Sprint Retrospective: inspect how clinical + engineering collaborated; agree 1–2 concrete improvements and updated working agreements for the next sprint | **Week 2 · Day 10** |

## PM judgment applied

- **Resolved the "Enable vs Equip" naming up front.** The framework labels the third E inconsistently; I standardized on **Enable** (noting Equip) and made it concretely about environments, access, and seed data so the team isn't blocked on day 3.
- **Split Evaluate into three touchpoints, not one.** AI parked all of Evaluate at sprint-end; I added a Day-6 mid-sprint audit-trail check because in a compliance product, finding the increment doesn't match the clinical workflow on Day 9 is too late.
- **Anchored Educate in our real domain, not generic onboarding.** I made the Clinical SME's hospital→home→specialist walkthrough and the audit-trail DoD the core of Educate, so cross-functional learning is specific to CareBridge.
- **Kept Empower honest about the Scrum Master role.** AI implied the SM assigns work; I corrected it so Empower means the team self-organizes and the SM clears blockers rather than directing — the distinction that makes the framework real.

_Reusable prompt: [prompt-library](../prompts/prompt-library.md) · Source technique: AI-Powered Agile workbook §2.3._
