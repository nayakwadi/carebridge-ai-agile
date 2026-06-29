# AI-Assisted Backlog Prioritization

*Course mapping : Workbook 1.1: Managing Agile Projects Using AI*

## Scenario

I have a 16-story CareBridge MVP backlog (`docs/product/product-backlog.md`) and two quarters to ship a pilot-ready product for three HIPAA-conscious health systems. I used AI as a scrum-master collaborator to turn the project context, OKRs, and technical dependencies into a defensible priority order : then applied PM judgment before committing.

## The prompt I used

```text
You are an expert Agile scrum master who understands the data required to prioritize the
backlog list. I will provide you with the project purpose and context information, analysis of
backlogged features and I want you to make a recommendation for how the features should be
prioritized. Here is the information on the project context and other data that is relevant to
prioritise the feature backlog.

[Project goal]
Ship a pilot-ready CareBridge MVP in 2 quarters: hospital care teams manage patients, care plans,
and tasks on a fully auditable platform, ready for a HIPAA-conscious pilot with 3 health systems.
The platform exists to cut avoidable 30-day readmissions and improve care-transition follow-through.

[Emphasized features / OKRs]
- OKR-1: Reduce avoidable 30-day readmissions by 15% across 3 pilot health systems within 12 months.
- OKR-2: Achieve >=90% in-platform care-task completion rate.
- OKR-3: Reach HIPAA + SOC 2 Type II readiness before General Availability.
Because this is a HIPAA pilot, trust/compliance features are non-negotiable for go-live; the
clinical workspace is the daily-use core; insight features prove the OKRs.

[Technical dependencies]
- Auth (CB-7) is a hard prerequisite for RBAC (CB-8) and the audit trail (CB-9).
- Audit-trail completeness depends on the RBAC model being finalized early.
- The clinical chain is sequential: patient list (CB-1) -> patient record (CB-2) -> care plan (CB-3)
  -> tasks (CB-4) -> task board (CB-5) -> blocked state (CB-6).
- Notifications (CB-11/CB-12) depend on tasks/board existing.
- Dashboard (CB-13/CB-14) depends on task and audit data being captured.
- FHIR import (CB-15/CB-16) depends on pilot sites granting export access.

[Resource constraints]
- One cross-functional delivery team, fixed capacity, 2-week sprints, 2-quarter timebox.
- Current JWT auth is a demo stub and must be hardened.
- EU data-residency requires hosting that is not yet provisioned.

[Time-sensitive features]
- HIPAA controls (auth, RBAC, audit) must land before any real PHI touches the system.
- EU data-residency (CB-10) gates the Germany launch but not the US pilot.
- FHIR import (CB-15) is needed before pilot go-live so sites don't re-key records.

Given the purpose of each feature in the list and the relevant data shared here, please produce a
prioritised list of the following features: {CB-1 ... CB-16}. Provide a rationale for the
prioritisation recommendation you provide, and a recommendation for any additional information that
can better inform your prioritization recommendation.
```

## AI-generated output

**Prioritized backlog : CareBridge MVP**

| Rank | Story ID | Feature | Rationale |
|------|----------|---------|-----------|
| 1 | CB-7 | Authentication | Hard prerequisite. No PHI can touch the system without it; blocks RBAC and audit. Foundational to OKR-3. |
| 2 | CB-1 | Patient list (risk + status) | Root of the clinical data model and the first screen every coordinator opens. Everything downstream needs it. |
| 3 | CB-2 | Patient record detail | Required context before any task action; unblocks care plans. |
| 4 | CB-8 | Role-based access control | Must be finalized early because audit-trail correctness depends on it; core to the HIPAA pilot. |
| 5 | CB-9 | HIPAA audit trail | Non-negotiable for go-live and directly tied to OKR-3. Sequenced right after the access model it records. |
| 6 | CB-3 | Care plan creation | The shared-goal artifact; the heart of the value proposition. Unblocks tasks. |
| 7 | CB-4 | Care-plan tasks (assignee/priority/due) | Makes ownership explicit; prerequisite for the board, notifications, and dashboard. |
| 8 | CB-5 | Kanban task board | Primary daily-use surface; where OKR-2 task completion actually happens. |
| 9 | CB-6 | Blocked task state + reason | Small, high-leverage: surfaces stalls during the 30-day window so coordinators intervene. |
| 10 | CB-11 | Task-assigned notifications | Drives prompt action on new work; first half of the OKR-2 follow-through loop. |
| 11 | CB-12 | Overdue-task notifications | Closes the follow-through loop; protects against slippage in the critical window. |
| 12 | CB-15 | FHIR import | Needed before go-live so pilot sites don't re-key records, but gated by external export access : start discovery early, build once data is available. |
| 13 | CB-16 | FHIR validation / de-dup | Protects chart integrity; only meaningful once import (CB-15) exists. |
| 14 | CB-13 | Reporting / readmission dashboard | Proves OKR-1 and OKR-2, but needs task + audit data to exist first; value lands later in the pilot. |
| 15 | CB-14 | Dashboard risk/team filters | Enhancement to CB-13; defer until the base dashboard is in use. |
| 16 | CB-10 | EU data-residency | Critical for Germany but not for the US pilot. Time-box risk is real (hosting unprovisioned), so begin infra discovery in parallel but rank delivery last for the US-pilot-first MVP. |

**Sequencing notes from the AI**
- Compliance spine (CB-7 → CB-8 → CB-9) and the clinical spine (CB-1 → CB-5) can largely run in parallel across two squads; the ranking reflects dependency order, not strict calendar order.
- CB-10 and CB-15 both carry *external* dependencies (hosting; pilot-site credentials). Treat their discovery/spikes as early even though delivery ranks late.

### Additional information that would sharpen this

- **Per-site go-live order.** Is one of the three pilot health systems first? If so, that site's FHIR export readiness (CB-15) and any EU exposure (CB-10) could reorder mid-backlog items.
- **OKR-1 measurement source.** Will readmission outcomes come from inside CareBridge or from the health systems' claims/EHR data? This determines how much CB-13 must do and when it's truly needed.
- **Team capacity split.** Can we staff two parallel squads (clinical + compliance), or is it one stream? Parallelism materially changes whether ranks 1–9 are sequential or concurrent.
- **Auth hardening scope.** What's the gap between the demo JWT stub and pilot-grade auth (SSO? MFA? session policy)? This sizes CB-7 and could pull effort forward.
- **Regulatory trigger for CB-10.** Is any pilot site in or routing data through the EU during the MVP? If not, CB-10 can safely move to the post-MVP roadmap.

## PM judgment applied

- **Kept the compliance-first spine.** The AI correctly ranked auth/RBAC/audit (CB-7/8/9) ahead of most clinical features. For a HIPAA pilot that's right, and I committed it without change.
- **Challenged the dashboard ranking.** I pushed CB-13 down to rank 14 (the AI had floated it higher) because OKR-1 readmission data largely arrives from outside the platform and lags : so an early dashboard would have nothing real to show. I logged "OKR-1 measurement source" as an open question, exactly as the AI flagged.
- **Verified CB-10's late rank against business risk.** I accepted ranking EU data-residency last for delivery, but I overrode the implied "do it last" by scheduling an infra spike in Sprint 2 : the hosting lead time is the actual risk, not the build effort.
- **Carried the open questions into refinement.** The AI's "additional information" list became real backlog-refinement actions (per-site go-live order, capacity split, auth scope) rather than being treated as a finished answer.

---

_Reusable prompt: [prompt-library](../prompts/prompt-library.md) · Source technique: AI-Powered Agile workbook 1.1._
