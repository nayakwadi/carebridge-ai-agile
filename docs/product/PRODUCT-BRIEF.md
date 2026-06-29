<!-- Note: this brief intentionally contains ambiguities for the Ch1.3 AI requirements-refinement exercise to surface. -->

# CareBridge : Product Brief & Project Charter (MVP)

**Document type:** Project charter / product vision
**Version:** 0.9 (draft for stakeholder review)
**Owner:** Product Owner, CareBridge MVP
**Status:** Pending sign-off from Clinical, Compliance, and Product leadership

---

## 1. Background

CareBridge Health is a mid-sized US digital-health firm that builds tooling for hospital care teams. Today, care coordination across transitions of care : hospital to home to specialist : is fragmented across phone calls, faxes, spreadsheets, and disconnected EHR modules. Tasks fall through the cracks during the highest-risk window for a patient: the first 30 days after discharge.

CareBridge is an AI-assisted patient care-coordination platform. It gives a care team a single shared view of their patients, structured care plans, and a task board that makes "who owns what, by when" unambiguous : with a full audit trail behind it. The MVP targets a HIPAA-conscious pilot with three health systems, and the company is simultaneously preparing to expand into the EU (Germany) and Canada.

## 2. Problem statement

Avoidable 30-day readmissions are costly to health systems and harmful to patients. Care teams lack a single coordinated workspace, so handoffs are inconsistent, follow-up tasks are missed, and there is no reliable record of who accessed or changed a patient's information. Leadership needs a tool that (a) makes care-transition work visible and accountable, and (b) stands up to HIPAA scrutiny from day one.

## 3. Objectives & success metrics

The MVP is anchored to three organizational OKRs:

| # | Objective | Success metric | Target | Timeframe |
|---|-----------|----------------|--------|-----------|
| O1 | Reduce avoidable readmissions | Reduction in avoidable 30-day readmission rate | 15% | Across 3 pilot health systems within 12 months |
| O2 | Drive task follow-through | In-platform care-task completion rate | ≥ 90% | Steady-state during pilot |
| O3 | Be audit-ready | HIPAA + SOC 2 Type II readiness | Achieved before General Availability | Before GA |
| O4 | Earn care-team adoption | Care-team weekly active usage | (to be set after baseline) | During pilot |

These objectives are deliberately outcome-oriented; the engineering scope below is the smallest surface area we believe can move them.

## 4. Scope

### In scope (MVP)
- Patient management: patient list, demographics, primary condition, risk level, status.
- Care plans: structured plans with goal, status, start/target dates.
- Care-plan task board: a Kanban board (todo / in progress / blocked / done) with priority, assignee, and due date.
- Authentication and role-based access control (RBAC) for the five care-team roles.
- HIPAA-style audit trail capturing read/write access to patient data.
- Notifications for assigned and overdue tasks.
- A readmission/reporting dashboard for care leads.
- FHIR import to bootstrap patient records from existing systems.
- EU data-residency support to enable the Germany expansion.

### Out of scope (MVP)
- Direct, bi-directional EHR write-back.
- Patient-facing mobile application.
- Billing, claims, and revenue-cycle features.
- Predictive/ML readmission risk scoring (risk level is entered, not modeled, in the MVP).
- Canada-specific data-residency (planned for a later release).

## 5. Expected benefits

- **Fewer avoidable readmissions.** By making transition tasks visible and owned, we expect a significant reduction in readmissions and a meaningful improvement in patient outcomes across the pilot sites.
- **Faster, more reliable handoffs.** A shared task board replaces ad-hoc phone/fax coordination, reducing missed follow-ups.
- **Audit confidence.** A complete access trail lets compliance demonstrate HIPAA controls without manual reconstruction.
- **Operational savings.** Less time spent on manual coordination frees care-coordinator capacity for direct patient work, which should lower coordination cost per patient.
- **A foundation for EU growth.** Data-residency support unblocks the Germany launch and de-risks the broader international roadmap.

## 6. Stakeholders

| Stakeholder | Interest in CareBridge |
|-------------|------------------------|
| Clinical staff (physicians, nurses, care coordinators) | Want a fast, low-friction tool that fits real care-transition workflows; resist anything that adds clicks or documentation burden. |
| Compliance / Privacy office | Owns HIPAA and SOC 2 posture; wants comprehensive audit logging and tight access controls, even at the cost of workflow speed. |
| Product leadership | Wants a pilot-ready MVP shipped in two quarters to prove value and unblock EU expansion. |
| Pilot health-system administrators | Want measurable readmission and efficiency improvements to justify continued investment. |
| Patients / caregivers | Benefit indirectly from better-coordinated, safer transitions of care. |
| Agile delivery team | Builds and operates the platform; needs clear, prioritized requirements within the timebox. |

## 7. Assumptions, constraints & dependencies

### Assumptions
- The three pilot health systems can supply patient data in a FHIR-compatible format for import.
- Care teams will adopt the platform as their primary coordination tool during the pilot rather than running it in parallel with existing tools.
- Pilot-site clinical workflows are similar enough that a single configuration serves all three.

### Constraints
- Delivery is timeboxed to two quarters (the MVP must be pilot-ready by end of Q2).
- The platform must meet HIPAA controls and be on a credible path to SOC 2 Type II.
- The delivery team runs two-week sprints with fixed capacity.

### Dependencies
- EU data-residency hosting must be available before the Germany launch.
- FHIR import depends on pilot sites granting export access and credentials.
- Audit-trail completeness depends on the access-control model being finalized early.

## 8. High-level timeline

| Quarter | Focus |
|---------|-------|
| Q1 | Auth/RBAC, patient management, care plans, task board, audit trail foundation. |
| Q2 | Notifications, reporting/readmission dashboard, FHIR import, EU data-residency, pilot hardening. |
| Post-MVP | Pilot rollout across 3 health systems; SOC 2 Type II evidence collection; GA readiness; Canada residency. |

---

_Prepared for stakeholder review. Sign-off required from Clinical, Compliance, and Product before backlog commitment._
