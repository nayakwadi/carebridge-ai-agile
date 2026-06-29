# AI-Assisted Requirements Refinement

*Course mapping : Workbook 1.3: Developing Agile Requirements with the Help of AI*

## Scenario

Before committing the CareBridge MVP backlog, I ran the draft Product Brief (`docs/product/PRODUCT-BRIEF.md`, v0.9) through AI as an experienced proof-reader/editor/PM to surface ambiguity, contradictions, and unstated assumptions : and specifically to probe for **potential stakeholder conflicts** that could derail the agile delivery later.

## The prompt I used

```text
As an experienced proof-reader, editor and project manager with over 20 years of experience,
analyze the following project document [the CareBridge Product Brief, docs/product/PRODUCT-BRIEF.md]
and look for areas of ambiguity, such as vague statements around cost savings or other expected
benefits, that could lead to misaligned stakeholder expectations down the road. Also look for
contradictions and other items that might result in shortcomings as an agile project moves
forward... are success metrics clearly defined with expected dollar amounts/production targets?...
anything in the text that implies an assumption has been made but isn't specifically identified
should be noted as an action to investigate... are there any statements or assumptions lacking
accountability or concrete measures? ... please investigate the following additional
characteristic: potential stakeholder conflicts.
```

## AI-generated output

**Requirements refinement findings : CareBridge Product Brief v0.9**

### 1. Ambiguities

- **F-1 : "A significant reduction in readmissions" is unquantified (5 Expected benefits).** The benefits section says CareBridge will deliver "a significant reduction in readmissions and a meaningful improvement in patient outcomes," yet the brief elsewhere (3, O1) commits to a precise **15%** target. The vague benefit language will set softer expectations than the OKR.
  *Recommended action:* Replace "significant reduction" with the committed figure ("the targeted 15% reduction in avoidable 30-day readmissions across the 3 pilot sites within 12 months") so 5 and 3 cannot drift apart.

- **F-2 : "Operational savings" / "lower coordination cost per patient" has no figure (5).** A cost-savings benefit is claimed with no dollar amount, baseline, or percentage. This is exactly the kind of vague cost-savings statement that misaligns expectations with health-system sponsors.
  *Recommended action:* Either quantify the expected coordination-cost reduction (with a baseline) or restate it as a hypothesis to be validated in the pilot, not a promised benefit.

### 2. Contradictions / inconsistencies

- **F-3 : Benefit language (5) understates the committed metric (3).** As noted in F-1, "significant reduction" (5) and "15% within 12 months" (3, O1) describe the same outcome at two different levels of specificity. Left unreconciled, clinical and product stakeholders may anchor on different numbers.
  *Recommended action:* Make 5 reference the OKR target verbatim; treat 3 as the single source of truth for the readmission number.

- **F-4 : "Audit-ready" scope is stated two ways.** 3/O3 commits to "HIPAA + SOC 2 Type II readiness before GA," while 4 (In scope) and the timeline (8) treat SOC 2 Type II as a *post-MVP* evidence-collection activity. This is a sequencing inconsistency, not an outright error, but it should be made explicit so no one assumes Type II is in the two-quarter MVP.
  *Recommended action:* State clearly that the MVP delivers HIPAA controls + SOC 2 *readiness/path*, with Type II attestation occurring post-MVP.

### 3. Implied-but-unstated assumptions

- **F-5 : The cost-savings benefit assumes today's coordination cost is measured.** 5 promises "lower coordination cost per patient," which silently assumes a current, baselined coordination-cost figure exists to improve upon. The brief never states that baseline or who owns it. Per the prompt, an implied assumption must become an action to investigate.
  *Recommended action:* Add an explicit assumption ("a current coordination-cost-per-patient baseline is available from pilot sites") and an action to confirm it before any savings claim is made externally.

- **F-6 : "Care teams will adopt CareBridge as their primary tool" is assumed but adoption isn't measured.** 7 lists the primary-tool-adoption assumption, and O4 (adoption) exists : but O4 has no target (see F-7). The benefits all depend on adoption that the brief assumes rather than commits to measuring.
  *Recommended action:* Tie the 7 adoption assumption to a measurable O4 target so adoption is tracked, not hoped for.

### 4. Accountability / measurement gaps

- **F-7 : O4 (care-team weekly active usage) has no target (3).** The success-metrics table leaves O4's target as "(to be set after baseline)." An objective with no target cannot be passed or failed and provides no accountability.
  *Recommended action:* Set a provisional target now (e.g., a defined weekly-active threshold per pilot site) and revise after baseline, rather than shipping the charter with an open target.

- **F-8 : No named owner per objective.** 3 lists objectives but assigns no accountable owner to each (e.g., who owns O1's readmission outcome vs. O2's task-completion). Without owners, OKR accountability is diffuse.
  *Recommended action:* Add an "Owner" column to the 3 table (e.g., Health-System Admin sponsor for O1, Product Owner for O2, Compliance for O3).

### 5. Stakeholder-conflict risks *(requested characteristic)*

- **F-9 : Clinical low-friction vs. Compliance comprehensive-logging vs. Product timebox : a three-way latent conflict (6).** The stakeholder table itself encodes the tension: clinical staff "resist anything that adds clicks or documentation burden," Compliance "wants comprehensive audit logging and tight access controls, **even at the cost of workflow speed**," and Product "wants a pilot-ready MVP shipped in two quarters." These three goals are in direct competition : every audit/RBAC control Compliance adds is friction Clinical resists, and reconciling both eats the timebox Product is protecting. The brief names all three interests but never states how the trade-off will be resolved or who decides.
  *Recommended action:* Add an explicit decision/escalation mechanism (e.g., a named arbiter or a standing trade-off forum) and a guiding principle for the MVP : for example, "compliance controls are non-negotiable; friction is minimized within that constraint." Confirm sign-off from all three (the brief already says sign-off is pending from Clinical, Compliance, and Product : make resolving this conflict a precondition of that sign-off).

## PM judgment applied

- **Validated each finding against the source.** I confirmed F-1/F-3 against 5 vs 3, F-7 against the O4 row, and F-9 against the 6 wording before accepting any of them : the AI doesn't get to invent gaps. All nine traced to real text.
- **Promoted F-9 to a sign-off blocker.** I agreed with the AI that the clinical/compliance/product trade-off is the highest-risk item and made resolving it a precondition of charter sign-off, not just an edit.
- **Kept F-4 as a clarification, not a defect.** The SOC 2 readiness-vs-attestation point is a wording fix, not a scope error; I downgraded it from "contradiction" to "make explicit" so we don't over-correct the timeline.
- **Turned implied assumptions into backlog/refinement actions.** F-5 (cost baseline) and F-6 (adoption measurement) became investigate-actions feeding the next refinement session rather than silent edits to the brief.

---

_Reusable prompt: [prompt-library](../prompts/prompt-library.md) · Source technique: AI-Powered Agile workbook 1.3._
