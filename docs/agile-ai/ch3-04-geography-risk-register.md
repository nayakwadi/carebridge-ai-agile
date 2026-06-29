# Multi-Geography Regulatory Risk Register (US / EU / Canada)

*Course mapping — Workbook §3.4: Agile projects in multiple geographies*

## Scenario

With the CareBridge expansion into Germany and Canada, the same care-coordination platform now spans three regulatory regions and a distributed delivery team. I used AI to draft a project-management risk register that crosses geography, regulation, and concrete PM actions — so that data residency, cross-border transfer, consent, and breach-timeline differences become *managed backlog items* rather than launch-week surprises.

## The prompt I used

```text
As an experienced project manager with over 20 years of experience working in
regulated industries, I'd like a list of common risks project managers need to
manage for projects that touch upon a regulatory area. Present the entire list of
risks as output in a table, with the industry, regulation name, geography/country,
and a list of risks project managers need to handle (one risk per line).

(regulation) covering digital health
[geography] = US, EU, Canada
```

## AI-generated output

| Industry | Regulation | Geography | Risk | Mitigation / PM action |
|---|---|---|---|---|
| Digital health | HIPAA / HITECH | US | PHI exposure via insufficient access controls or audit gaps | Enforce least-privilege; rely on the platform's READ/WRITE `audit_log` trail; add HIPAA acceptance criteria to Definition of Done |
| Digital health | GDPR | EU (Germany) | **Data residency** — health data must stay in-region; US-hosted services breach expectations | Provision EU-region (Frankfurt) data tier; document where PHI is stored/processed per environment |
| Digital health | GDPR (Schrems II) | EU → US | **Cross-border transfer** invalidated without a valid mechanism | Adopt **Standard Contractual Clauses (SCCs)** + transfer impact assessment; minimize/avoid transatlantic PHI flows; prefer EU-local processing |
| Digital health | GDPR / PHIPA / HIPAA | EU, Canada, US | **Consent management** divergence — granularity and lawful basis differ by region | Build a configurable consent model; capture purpose + lawful basis per record; let the Clinical SME validate clinical consent flows |
| Digital health | Breach-notification rules | US / EU / Canada | **Breach-notification timeline differences** (GDPR 72h; HIPAA "without unreasonable delay," ≤60 days; PIPEDA/PHIPA "as soon as feasible") | Maintain a per-region incident-response runbook keyed to the *tightest* clock (72h); pre-draft notification templates; rehearse with DevOps/SRE |
| Digital health | 21st Century Cures Act / EHDS | US / EU | **Interoperability mandates** — FHIR/HL7 exchange and anti-information-blocking obligations | Standardize on **HL7 FHIR** resources for patient/care-plan data; plan API conformance work as backlog epics, not afterthoughts |
| Digital health | EU AI Act | EU | AI features in a clinical context may trigger high-risk conformity obligations | Inventory AI/ML usage; run a risk classification early; gate AI-assisted features behind documented evaluation and human oversight |
| Digital health | DiGA / BfArM | EU (Germany) | Reimbursement/market-access risk — failing BfArM evidence, security, or data-protection criteria | Map BfArM requirements to the roadmap before German launch; engage local regulatory counsel; treat as a release gate |
| Digital health | PIPEDA / PHIPA | Canada | Provincial vs. federal scope confusion (e.g., Ontario PHIPA custodianship) | Confirm which law governs each customer/province; assign a data custodian role; verify cross-border accountability clauses |
| Digital health | All regions | US / EU / Canada | **Localization & translation** — clinical UI/content must be accurate in German/French; mistranslation is a safety risk | Plan i18n early (de-DE, fr-CA, en-CA); have clinicians review translated clinical terms; never machine-translate patient-safety copy unreviewed |
| Digital health | All regions | Global team | **Distributed / multi-time-zone staffing** — slow feedback loops, handoff gaps, fragmented agile culture | Define core overlap hours; async-first decision log; federated working agreements with thin region-specific guardrails (per §3.1) |
| Digital health | SOC 2 / ISO 27001 | US / EU / Canada | Customer trust & procurement blockers without recognized attestation | Sequence SOC 2 Type II evidence collection into sprints (OKR 3); reuse ISO 27001 controls to satisfy overlapping EU expectations |

## PM judgment applied

- **Kept** the cross-border transfer and breach-timeline rows as top priorities — Schrems II/SCCs and the GDPR 72-hour clock are the risks most likely to stop a German launch, and I made the mitigation column actionable for DevOps/SRE rather than abstract.
- **Added a "Mitigation / PM action" column** the raw prompt didn't ask for, because a risk list without owned actions is just a worry list; every row now points to a concrete backlog or runbook item.
- **Challenged the "one consent model" temptation**: I had the AI keep consent *configurable per region* rather than lowest-common-denominator, since collapsing GDPR/PHIPA/HIPAA consent into one rule would either over-collect or under-protect.
- **Verified** the interoperability row maps to our actual data model — patient and care-plan entities exchange cleanly as HL7 FHIR resources — so the Cures Act/EHDS mandate becomes a sized epic, not a vague obligation. Region/timeline specifics still get confirmed with counsel before launch.

_Reusable prompt: [prompt-library](../prompts/prompt-library.md) · Source technique: AI-Powered Agile workbook §3.4._
