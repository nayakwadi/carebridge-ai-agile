# Using AI to Reinforce CareBridge's Agile Culture

*Course mapping : Workbook 3.2: How AI can help reinforce agile culture*

## Scenario

Naming the inhibitors (3.1) was step one; reinforcing the culture is the ongoing work. I used AI to draft three concrete, runnable programs for the CareBridge cross-functional delivery team and leadership: an education program on agile principles and intrinsic motivation, a servant-leadership program, and a recurring collaboration survey anchored to our organizational OKRs.

## The prompt I used

```text
#ROLE
Act as an Agile coach and organizational-development facilitator for a regulated
digital-health company (CareBridge Health), building the AI-assisted CareBridge
care-coordination platform on 2-week sprints.

#AUDIENCE
The CareBridge cross-functional delivery team (Product Owner, Scrum Master, Clinical
SME / nurse-informaticist, Frontend, Backend, Data/Platform, QA/Automation Engineers,
UX Designer, DevOps/SRE) and their leadership.

#TASK
Produce THREE deliverables that reinforce an agile culture:
1. An EDUCATION PROGRAM on agile principles and intrinsic motivation (autonomy,
   mastery, purpose): activities, participants, format, and how to execute it.
2. A SERVANT-LEADERSHIP PROGRAM to help leads master serving the team, facilitating
   collaboration, and shared decision-making.
3. A COLLABORATION SURVEY (8-10 questions, mix of multiple-choice and open-ended)
   to gauge collaboration and surface obstacles.

#SUCCESS METRICS (use the CareBridge organizational OKRs to anchor the survey)
- Reduce avoidable 30-day readmissions by 15% across 3 pilot health systems in 12 months.
- Achieve >=90% care-task completion rate within the platform.
- Reach HIPAA + SOC 2 Type II readiness before General Availability.

#FORMAT
Use three clearly separated sections with headers, bullets, and a numbered survey.
Keep it concrete and immediately runnable by a Scrum Master.
```

## AI-generated output

### Education program

**"Agile by Principle, Not Process" : a 4-session learning series**

- **Purpose / framing:** Move the team from following ceremonies to understanding *why* : the Agile Manifesto values plus intrinsic motivation (autonomy, mastery, purpose) applied to a patient-facing product.
- **Participants:** Whole delivery team; the nurse-informaticist co-leads the clinical-context session; leadership attends Session 1 and Session 4 only (to signal sponsorship without dominating).
- **Format:** Four 75-minute working sessions, one per sprint over 8 weeks; interactive (no lecture-only), each ending with one experiment the team commits to in the next sprint.
- **Session outline:**
  - **Session 1 : Why agile, here:** Manifesto values mapped to CareBridge's mission (cutting avoidable readmissions). Activity: each member writes the *purpose* of their role in one patient-impact sentence.
  - **Session 2 : Autonomy & decision rights:** Delegation poker on real decisions (e.g., when can the team change the care-plan Kanban without escalation?). Output: a one-page decision-rights map.
  - **Session 3 : Mastery & flow:** Slicing patient-facing work small and safely; WIP limits on the board; a kata on writing a thin, testable, *auditable* story.
  - **Session 4 : Purpose & feedback loops:** Connect sprint output to the OKRs (readmissions, task-completion). Activity: map last sprint's increments to which OKR they moved.
- **How to execute:** Scrum Master owns scheduling inside existing sprint cadence; pre-read is one short article + the relevant CareBridge artifact; each session produces a visible artifact (decision map, sliced story, OKR linkage) so learning lands in the actual workflow.

### Servant-leadership program

**"Serve the Team" : a leadership practice track for the Scrum Master, PO, and tech/clinical leads**

- **Purpose:** Help leads master servant leadership : removing impediments, facilitating collaboration, and enabling shared decision-making rather than directing.
- **Participants:** Scrum Master (facilitator), Product Owner, lead engineers, Clinical SME, DevOps/SRE lead; sponsored by leadership.
- **Format:** Six bi-weekly 60-minute peer-coaching circles + on-the-job practice between sessions.
- **Core practices covered:**
  - **Serving the team:** Run a recurring impediment board; leads measure themselves on *blockers removed per sprint*, not tasks assigned.
  - **Facilitating collaboration:** Practice neutral facilitation (timeboxing, drawing out quiet voices like QA and the nurse-informaticist, separating idea-generation from decision).
  - **Shared decision-making:** Adopt consent-based decisions for team-level calls; reserve escalation for genuine clinical-safety or regulatory questions only.
  - **Psychological safety:** Leads model fallibility ("here's what I got wrong"); blameless retros; protect people who raise risks early.
- **How to execute:** Each session pairs a short concept with a live scenario from the current sprint; leads commit to one behavior change and report back next circle. Scrum Master tracks a simple before/after pulse (impediments removed, decisions made at team level vs. escalated).

### Collaboration survey

**CareBridge Cross-Functional Collaboration Pulse** : run anonymously each sprint review; mix of multiple-choice (MC) and open-ended (OE). Anchored to our OKRs so results tie to outcomes, not vibes.

1. **(MC)** This sprint, I had the information and access I needed from other roles to do my work well. *(Strongly disagree → Strongly agree, 1–5)*
2. **(MC)** Clinical context (from our nurse-informaticist) reached engineering early enough to avoid rework on patient-facing stories. *(1–5)*
3. **(MC)** Compliance/audit work (HIPAA, SOC 2) was planned and visible in the sprint rather than a surprise. *(1–5)* : *anchors OKR 3: HIPAA + SOC 2 Type II readiness.*
4. **(MC)** I felt safe raising a defect, risk, or doubt about a patient-facing feature without fear of blame. *(1–5)*
5. **(MC)** Decisions that the team should own were made by the team, not escalated unnecessarily. *(1–5)*
6. **(MC)** Our increments this sprint moved at least one organizational OKR (readmissions ↓15%, ≥90% care-task completion, or compliance readiness). *(Yes / Partly / No / Unsure)*
7. **(OE)** What was the single biggest collaboration *obstacle* you hit this sprint, and which roles did it sit between?
8. **(OE)** Where did clinical and engineering understanding diverge, and what would have closed the gap sooner?
9. **(OE)** What is one thing leadership or the Scrum Master could *stop, start, or continue* to help us hit the ≥90% care-task-completion target?
10. **(OE)** If you could change one thing about how we make decisions or handle compliance work next sprint, what would it be?

*Scoring note: track the MC averages sprint-over-sprint as a collaboration trendline; route every OE obstacle into the retro's action list with an owner.*

## PM judgment applied

- **Kept** the three-program structure and the intrinsic-motivation lens (autonomy/mastery/purpose) : it's the right backbone, and tying Session 4 directly to our OKRs makes the education program defensible to leadership.
- **Changed** the survey from generic "team health" to **OKR-anchored** questions: I rewrote Q3 and Q6 to explicitly test compliance visibility (OKR 3) and OKR-linked increments, because a culture survey that doesn't connect to outcomes won't survive budget scrutiny.
- **Challenged** scope creep on the servant-leadership track: the AI proposed a multi-month curriculum; I capped it at six 60-minute circles that fit *inside* existing cadence so it doesn't compete with delivery.
- **Verified** psychological safety shows up in *both* the program and the survey (Q4) : that's the inhibitor I most want to move, so I made sure it's measured, not just trained.

_Reusable prompt: [prompt-library](../prompts/prompt-library.md) · Source technique: AI-Powered Agile workbook 3.2._
