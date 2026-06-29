# Staffing the CareBridge Delivery Team

*Course mapping : Workbook 2.1: Using AI to scope an Agile team's roles, skills, and capabilities*

## Scenario

I'm standing up the Agile delivery team that will build the **CareBridge** patient care-coordination platform. The pilot-ready MVP must ship in 2 quarters and clear a HIPAA-conscious bar for 3 health systems. Before I open a single requisition, I used AI as a thinking partner to pressure-test which roles I actually need : and which I can combine for a lean pilot squad without breaking delivery.

## The prompt I used

```text
You are a highly experienced scrum master who has a reputation for running
successful agile projects. You are asked to put an agile project team
together. The outcome for the initiative is to ship a pilot-ready MVP of
CareBridge : an AI-assisted patient care-coordination platform : within
2 quarters, so that care teams can manage patients, care plans, and tasks
with a fully auditable trail, ready for a HIPAA-conscious pilot with 3 US
health systems. I am tasked with putting the right team in place, what
considerations and roles should I consider.

(then)
Create a table showing the team, skills and capabilities of the team members
in three columns: team member | skillset | capabilities.

(then)
If you were to combine any of these roles, can you do another iteration with
combined skill sets?
```

## AI-generated output

### (a) Considerations before naming roles

- **Regulatory gravity is non-negotiable.** Because we touch PHI and target HIPAA + SOC 2 Type II readiness before GA, every role needs a baseline of privacy/security literacy, and we need clinical correctness baked in : not bolted on. Staff a **Clinical SME** as a first-class team member, not an occasional reviewer.
- **Small, cross-functional, full-stack delivery.** A 2-week-sprint cadence and a 2-quarter horizon argue for one tight squad that can take a vertical slice (UI → API → data → audit trail) from idea to done, rather than handoff-heavy specialist silos.
- **The auditable trail is a product feature, not plumbing.** It needs deliberate ownership across Backend, Data, and QA : so design the team to cover audit logging as an explicit Definition-of-Done item.
- **Pilot operations matter early.** Three health systems means real environments, deployments, and incident response from week one : DevOps/SRE capability cannot wait until "after MVP."
- **Empowered Product Ownership.** With three pilot customers pulling in different directions, a single decisive **Product Owner** must own the backlog and say no, or scope will sprawl past two quarters.
- **Capacity realism.** Plan for sustainable pace, on-call rotation for the pilot, and slack for the discovery and compliance work that always runs hot in healthcare.

### (b) Full CareBridge delivery team

| Team member | Skillset | Capabilities |
|---|---|---|
| **Product Owner** | Healthcare product strategy, backlog management, stakeholder alignment, OKR framing | Translates the "15% readmission reduction" outcome into a prioritized, sliced backlog; owns scope and the "no"; runs reviews with the 3 pilot systems |
| **Scrum Master** | Agile facilitation, coaching, impediment removal, metrics (velocity, flow) | Runs the 2-week cadence; protects focus; surfaces and clears blockers; coaches the team to a healthy WIP and a strong Definition of Done |
| **Clinical SME (Nurse-Informaticist)** | Clinical workflows, care-transition domain, HIPAA awareness, terminology | Validates that care-plan and task models match real bedside-to-home workflows; reviews stories for clinical safety and correctness |
| **Frontend Engineer** | React + TypeScript, Vite, accessibility, component design | Builds the care-team dashboard, patient list, and care-plan Kanban board; ensures usable, accessible clinical UI under load |
| **Backend Engineer** | Python/FastAPI, REST design, JWT auth, audit-logging middleware | Implements the API, authz, and the HIPAA-style audit trail; owns service correctness and performance |
| **Data/Platform Engineer** | PostgreSQL, data modeling, migrations, seeding, Redis caching | Designs the patient/care-plan/task schema; owns migrations, seed data, and cache strategy; safeguards data integrity |
| **QA/Automation Engineer** | Test automation, API/E2E testing, security test cases | Builds the regression and audit-trail test suites; verifies READ/WRITE logging; gates releases against the DoD |
| **UX Designer** | Clinical UX research, interaction design, prototyping | Researches care-team workflows; designs flows for the dashboard and Kanban; reduces clicks at the point of care |
| **DevOps/SRE** | Docker Compose, CI/CD, observability, incident response | Owns one-command orchestration, pilot environments, deployment pipeline, and on-call readiness for 3 live systems |

### (c) Combined roles : lean pilot squad iteration

For the pilot phase I asked AI to collapse the nine roles into a leaner squad where one person credibly carries two adjacent skill sets:

| Combined role | Merged skillset | Capabilities |
|---|---|---|
| **Delivery Lead** (Scrum Master + Product Owner support) | Agile facilitation + backlog stewardship | Facilitates the cadence *and* keeps the backlog groomed; works with the PO on prioritization. *(Note: I challenged a full PO+SM merge : see PM judgment.)* |
| **Full-Stack Engineer** (Frontend + Backend) | React/TS + FastAPI across the vertical slice | Ships UI-to-API features end to end; ideal for thin vertical slices in early sprints |
| **Data/Platform + DevOps Engineer** | PostgreSQL/Redis + Docker/CI/CD/observability | Owns the data tier *and* the runtime: schema, migrations, orchestration, and pilot deployments |
| **Clinical SME + UX Designer** | Clinical domain + interaction design | Pairs clinical correctness with usability; runs care-team research and validates flows in one voice |
| **QA/Automation Engineer** | Test automation + security testing | Kept standalone : quality and audit verification stays independent of build |

This lean squad takes the team from 9 to ~5–6 people for the pilot, then re-splits as the platform scales toward GA.

## PM judgment applied

- **Kept the Clinical SME as a dedicated role even in the lean squad.** AI was willing to fold clinical review entirely into other roles; I refused : in a PHI product, clinical correctness is a safety control, not a nice-to-have.
- **Challenged the Product Owner + Scrum Master merge.** AI offered to combine them; I split that combination because the PO's "own the scope, say no to 3 customers" mandate conflicts with the Scrum Master's neutral, team-serving stance. I kept PO accountable and only shared facilitation load.
- **Verified the Full-Stack merge against our actual stack.** Because the codebase is React/TS front and FastAPI back, a genuine full-stack engineer is realistic here : I confirmed the combination matches our 3-tier architecture rather than accepting it on faith.
- **Added pilot on-call to DevOps capabilities.** AI under-weighted operations; I made incident readiness for 3 live health systems an explicit week-one capability, not a post-MVP afterthought.

_Reusable prompt: [prompt-library](../prompts/prompt-library.md) · Source technique: AI-Powered Agile workbook 2.1._
