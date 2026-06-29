# Digital-Health Regulatory Register (US / EU / Canada)

*Course mapping : Workbook 3.3: Agile in regulatory environments*

## Scenario

CareBridge Health is taking the platform from US-only into Germany and Canada, which means our delivery team needs a shared, plain-language map of the regulations that govern a patient-data product across all three regions. I used AI to generate a first-pass regulatory register so the Product Owner, Clinical SME, and DevOps/SRE could see the full landscape on one page before we wired any of it into Definition-of-Done acceptance criteria.

## The prompt I used

```text
I require a comprehensive list of regulations that exist in a given [industry]
environment, presented as a table with the legal name of the regulation, the context
for the regulation (for example data management), the latest year the regulation has
been updated, and the geographical region the regulation covers.

[industry] = digital health / health IT
(region) = US, EU, Canada
```

## AI-generated output

> **Note:** "Last updated" years below are AI-suggested approximations and **must be verified** against the primary source before any compliance decision : confirming currency is a PM responsibility, not the model's.

| Regulation / Framework | Context | Last updated (approx) | Region |
|---|---|---|---|
| **HIPAA** (Health Insurance Portability and Accountability Act) : Privacy & Security Rules | Protected health information (PHI) privacy, security safeguards, breach notification | 2013 (Omnibus Rule); Security Rule update proposed 2024–2025 | US |
| **HITECH Act** | Strengthens HIPAA enforcement; promotes EHR adoption; breach-notification teeth | 2009 (with ongoing HHS enforcement updates) | US |
| **21st Century Cures Act : ONC Information Blocking / interoperability** | Prohibits information blocking; mandates patient access to electronic health information (EHI) via standardized APIs | 2020 final rule; HTI-1/HTI-2 updates 2023–2024 | US |
| **FDA Software as a Medical Device (SaMD) guidance** | Regulatory status of clinical software; risk categorization; predetermined change control for AI/ML | 2019 framework; AI/ML guidance updated 2023–2025 | US |
| **GDPR** (General Data Protection Regulation) | Lawful basis, consent, data-subject rights, cross-border transfer of personal/health data | 2018 (in force); ongoing EDPB guidance | EU |
| **EU AI Act** | Risk-based obligations for AI systems; health-related/high-risk use cases face conformity duties | 2024 (adopted); phased application 2025–2027 | EU |
| **EHDS** (European Health Data Space) | Cross-border secondary use and sharing of electronic health data; EHR interoperability | 2024–2025 (regulation adopted, phased rollout) | EU |
| **Germany : DiGA / DVG (BfArM Fast-Track)** | Reimbursable digital health applications; BfArM evaluation for safety, data protection, evidence | 2019 DVG; DiGA guidance updated 2023–2024 | EU (Germany) |
| **PIPEDA** (Personal Information Protection and Electronic Documents Act) | Federal commercial privacy; consent, safeguards, cross-border accountability | 2019 (amendments); modernization via Bill C-27 in progress | Canada (federal) |
| **PHIPA** (Personal Health Information Protection Act) | Provincial health-information custodianship, consent, breach reporting | 2004; amended through ~2020–2021 | Canada (Ontario) |
| **SOC 2 (Type II)** : *trust-services framework* | Independent attestation of security, availability, confidentiality controls over time | AICPA TSC 2017, revised 2022 | US-origin, used globally |
| **ISO/IEC 27001** : *framework* | Information security management system (ISMS) certification | 2022 revision | International |
| **HITRUST CSF** : *framework* | Healthcare-tailored, certifiable control framework harmonizing HIPAA/ISO/NIST | CSF v11.x, updated 2023–2024 | US-origin, used globally |

## PM judgment applied

- **Flagged every year as "verify"** : I will not let an AI-suggested date drive a compliance commitment; the Clinical SME and I confirm each "last updated" against BfArM, ONC, EDPB, and the OPC before it informs acceptance criteria.
- **Kept the framework/regulation split clear**: SOC 2, ISO 27001, and HITRUST are control *frameworks*, not laws : I labeled them as such so the team doesn't treat an attestation like a statutory mandate (this also directly serves OKR 3: HIPAA + SOC 2 Type II readiness).
- **Added** Germany-specific DiGA/BfArM and Ontario PHIPA rows because "EU" and "Canada" alone hide the rules that actually bite during our Germany and Canada expansion.
- **Challenged completeness, not just accuracy**: I treat this as a living register owned in the repo, re-run each quarter, with the EU AI Act and EHDS phased timelines watched closely since their obligations land *during* our pilot window.

_Reusable prompt: [prompt-library](../prompts/prompt-library.md) · Source technique: AI-Powered Agile workbook 3.3._
