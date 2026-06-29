# Job Description — Senior Backend Engineer, Care Platform

*Course mapping — Workbook §2.1: Using a structured ROLE/GOAL/SKILLS prompt to draft a hiring artifact*

## Scenario

The CareBridge backend is the spine of the platform — it owns the FastAPI REST API, JWT auth, and the HIPAA-style audit-logging middleware that makes the whole product auditable. I need to hire a **Senior Backend Engineer** who can carry that responsibility through the pilot. Rather than recycle a generic template, I used a structured AI prompt to draft a job description grounded in our real stack and compliance bar.

## The prompt I used

```text
#ROLE
You are a highly experienced Recruitment professional who writes compelling,
honest job descriptions that attract strong engineers without overselling.

#GOAL
Put a job description together for a <#JOB>, for the <#JOB OUTCOME> in the
style of <#EXAMPLE1>/<#EXAMPLE2>. Here is a breakdown of the <#SKILLS> and
<#CAPABILITIES> needed for the <#JOB>.

#JOB = Senior Backend Engineer — Care Platform (FastAPI/PostgreSQL, healthcare)
#JOB OUTCOME = own and harden the CareBridge REST API, JWT auth, and HIPAA-style
  audit trail so 3 pilot health systems can coordinate patient care with a fully
  auditable record, on the path to HIPAA + SOC 2 Type II readiness before GA.
#EXAMPLE1 = a modern digital-health scale-up JD: mission-led, plain language, no jargon soup.
#EXAMPLE2 = a senior IC posting that leads with impact and ownership, not a tech laundry list.
#SKILLS = Python, FastAPI, PostgreSQL, REST API design, JWT/authn-authz,
  audit logging, Redis caching, Docker, testing.
#CAPABILITIES = ships secure auditable services; models clinical data correctly;
  reasons about PHI/compliance; mentors; partners with a Clinical SME.

(then)
Using bullet points, condense the complex responsibilities of a Senior Backend
Engineer — Care Platform into concise, scannable descriptions.

(then)
Suggest alternative job titles for this role that appeal to modern candidates.
```

## AI-generated output

### Senior Backend Engineer — Care Platform (FastAPI / PostgreSQL)

**CareBridge Health · Remote (US) with EU/Canada expansion · Full-time**

**Why this role matters.** CareBridge helps hospital care teams coordinate patients across the riskiest moments — the handoffs from hospital to home to specialist. Our goal is concrete: cut avoidable 30-day readmissions by 15% across our first three pilot health systems. You'll own the backend that makes every care plan, task, and access event trustworthy and auditable. In a product handling protected health information, that's not plumbing — it's the foundation of safety and trust.

**What you'll own.** You'll be the senior engineer accountable for the CareBridge REST API built on **FastAPI**, backed by **PostgreSQL** and **Redis**. You'll harden **JWT-based auth**, evolve our **HIPAA-style audit-logging middleware** (the READ/WRITE access trail), and model clinical entities — patients, care plans, tasks — so they reflect how real care teams work. You'll partner daily with our Clinical SME, Data Engineer, and QA to take the platform from pilot to **HIPAA + SOC 2 Type II readiness** before General Availability.

**You'll thrive here if you have.**

- 5+ years building production backend services in **Python**, with deep **FastAPI** (or comparable async framework) experience.
- Strong **REST API design** and **PostgreSQL** data-modeling skills, including migrations and query performance.
- Hands-on experience with **authentication/authorization** (JWT, sessions) and a security-first instinct.
- Comfort with **audit logging, PHI handling, or regulated environments** (HIPAA, SOC 2, GDPR) — or eagerness to go deep fast.
- Familiarity with **Redis caching**, **Docker**, and automated **testing** as part of your default workflow.
- A track record of **mentoring** and raising the bar on a small, cross-functional team.

**Nice to have.** Prior digital-health or clinical-systems experience; exposure to EU (Germany) / Canada data-residency requirements.

### Condensed, scannable responsibilities

- **Own the API:** design, build, and maintain the FastAPI REST services powering the care-team dashboard, patient list, and care-plan board.
- **Make it auditable:** evolve the HIPAA-style audit middleware so every READ/WRITE on PHI is captured, attributable, and tamper-evident.
- **Secure the front door:** harden JWT auth and authorization across roles (Physician, Nurse, Care Coordinator, Social Worker, Pharmacist).
- **Model the domain right:** shape patient, care-plan, and task data with the Clinical SME so it matches real care-transition workflows.
- **Keep it fast and reliable:** apply Redis caching and sensible PostgreSQL indexing to keep the API responsive at the point of care.
- **Ship with quality:** write tests, partner with QA on audit-trail verification, and uphold a security-aware Definition of Done.
- **Drive readiness:** contribute to HIPAA + SOC 2 Type II readiness ahead of GA.
- **Lift the team:** mentor engineers and review code with an eye for safety, clarity, and compliance.

### Alternative job titles for modern candidates

1. **Senior Backend Engineer, Patient Data & Trust**
2. **Senior Software Engineer — Care Platform (Python/FastAPI)**
3. **Staff Backend Engineer, Healthcare APIs**
4. **Senior Platform Engineer — Clinical Services**
5. **Senior Backend Engineer, Compliance-Critical Systems**

## PM judgment applied

- **Kept the mission-first framing, cut the buzzwords.** AI's first draft drifted toward a "rockstar ninja" tone; I held it to plain, honest language that a senior IC actually respects.
- **Verified every skill against our real stack.** I cross-checked the requirements against the implemented architecture (FastAPI, PostgreSQL, Redis, JWT, audit middleware, Docker) so we don't screen for skills the job doesn't use, or miss ones it does.
- **Promoted "audit logging / PHI" from nice-to-have to core.** AI buried compliance experience; given our SOC 2 / HIPAA bar, I moved security and audit literacy up front as a defining capability.
- **Challenged title inflation.** I rejected the "Staff" title as the primary posting for a pilot-stage team — it sets the wrong leveling expectation — but kept it in the alternatives list for candidate appeal and reach.

_Reusable prompt: [prompt-library](../prompts/prompt-library.md) · Source technique: AI-Powered Agile workbook §2.1._
