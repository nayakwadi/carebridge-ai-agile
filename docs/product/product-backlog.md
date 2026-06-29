# CareBridge — Product Backlog (MVP)

*Pilot-ready MVP in two quarters: care teams manage patients, care plans, and tasks on a fully auditable platform, ready for a HIPAA-conscious pilot with 3 health systems.*

**Priority column is intentionally `TBD` — see [ch1-01 backlog prioritization](../agile-ai/ch1-01-backlog-prioritization.md), which is the AI-assisted prioritization artifact that consumes this backlog as its input.**

## Epics

| Epic | Name | Description |
|------|------|-------------|
| E1 | Patient & Care-Plan Management | Core clinical workspace: patient records, care plans, and the care-plan task board. |
| E2 | Trust, Security & Compliance | Auth, RBAC, HIPAA audit trail, and EU data-residency — the controls that make a HIPAA-conscious pilot possible. |
| E3 | Coordination & Insight | Notifications and the reporting/readmission dashboard that drive task follow-through and prove outcomes. |
| E4 | Interoperability | FHIR import to bootstrap pilot data from existing health-system records. |

## User stories

| ID | Epic | User story | Priority | Notes (dependency / constraint / risk) |
|----|------|-----------|----------|----------------------------------------|
| CB-1 | E1 | As a Care Coordinator, I want to view and search a list of my patients with risk level and status, so that I can focus on the highest-risk transitions first. | TBD — see ch1-01 | Foundation for most clinical workflows; no upstream dependency. |
| CB-2 | E1 | As a Nurse, I want to open a patient record showing demographics, primary condition, and risk level, so that I have context before acting on a task. | TBD — see ch1-01 | Depends on CB-1 data model. |
| CB-3 | E1 | As a Physician, I want to create a care plan with a goal, status, and target date for a patient, so that the team works toward a shared objective. | TBD — see ch1-01 | Depends on CB-2; central to the value proposition. |
| CB-4 | E1 | As a Care Coordinator, I want to add tasks to a care plan with assignee, priority, and due date, so that responsibilities are explicit. | TBD — see ch1-01 | Depends on CB-3. |
| CB-5 | E1 | As a care-team member, I want a Kanban task board (todo / in progress / blocked / done) so that I can see and update work status at a glance. | TBD — see ch1-01 | Depends on CB-4; primary daily-use surface. |
| CB-6 | E1 | As a Nurse, I want to flag a task as "blocked" with a reason, so that coordinators can intervene quickly. | TBD — see ch1-01 | Depends on CB-5. |
| CB-7 | E2 | As any user, I want to authenticate before accessing patient data, so that PHI is not exposed to unauthenticated access. | TBD — see ch1-01 | Hard prerequisite for HIPAA pilot; blocks audit trail and RBAC. Current JWT is a demo stub — must be hardened. |
| CB-8 | E2 | As a Compliance officer, I want role-based access control across the five care-team roles, so that users only see and do what their role permits. | TBD — see ch1-01 | Depends on CB-7. Audit-trail completeness depends on this model being finalized early. |
| CB-9 | E2 | As a Compliance officer, I want every read and write to patient data recorded in an immutable audit log (actor, action, method, path, status), so that we can demonstrate HIPAA access controls. | TBD — see ch1-01 | Depends on CB-7/CB-8. Directly tied to OKR-3 (HIPAA + SOC 2 readiness). Risk: incomplete coverage undermines the whole pilot. |
| CB-10 | E2 | As a Compliance officer, I want patient data for EU pilots stored in an EU region, so that we satisfy German data-residency requirements. | TBD — see ch1-01 | Dependency: EU hosting must be provisioned. Gates the Germany expansion but not the US pilot. |
| CB-11 | E3 | As a Nurse, I want to be notified when a task is assigned to me, so that I act on new work promptly. | TBD — see ch1-01 | Depends on CB-4/CB-5. Supports OKR-2 (≥90% task completion). |
| CB-12 | E3 | As a Care Coordinator, I want to be notified when a task becomes overdue, so that follow-through doesn't slip during the 30-day window. | TBD — see ch1-01 | Depends on CB-11. |
| CB-13 | E3 | As a Health-System Administrator, I want a dashboard of care-task completion rate and readmission trends, so that I can judge whether the pilot is working. | TBD — see ch1-01 | Depends on CB-5/CB-9 data. Proves OKR-1 and OKR-2. Risk: readmission outcome data may lag and arrive from outside the platform. |
| CB-14 | E3 | As a Physician, I want to filter the dashboard by risk level and care team, so that I can spot at-risk cohorts. | TBD — see ch1-01 | Depends on CB-13. |
| CB-15 | E4 | As a Care Coordinator, I want to import patients from a pilot site via FHIR, so that we don't re-key records to start the pilot. | TBD — see ch1-01 | Dependency: pilot sites must grant FHIR export access/credentials. Assumption: data is FHIR-compatible (see brief). Risk: source-data quality. |
| CB-16 | E4 | As a Data/Platform Engineer, I want imported FHIR records validated and de-duplicated against existing patients, so that import doesn't create conflicting or duplicate charts. | TBD — see ch1-01 | Depends on CB-15. Risk: duplicate MRNs across source systems. |

---

_Backlog is the input to AI-assisted prioritization in [ch1-01-backlog-prioritization.md](../agile-ai/ch1-01-backlog-prioritization.md)._
