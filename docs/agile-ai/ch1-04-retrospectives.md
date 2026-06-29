# AI-Assisted Retrospectives & Lessons Learned

*Course mapping — Workbook §1.4: Agile Retrospectives and Lessons Learned with AI*

## Scenario

After CareBridge Sprint 6 — the sprint where the HIPAA audit trail (CB-9) and the Kanban task board (CB-5) both landed — I used AI to synthesize the team's raw retro notes and reaction votes into themes, a sentiment read, and committed action items, so the 60-minute retro produced decisions instead of just a wall of sticky notes.

## AI retrospective tooling considered

The workbook surveys purpose-built AI retro tools. I evaluated these before deciding to run the synthesis directly on our notes:

| Tool | One-line description |
|------|----------------------|
| TeamRetro | Facilitated retro boards with AI-generated summaries, grouping, and action tracking. |
| ScatterSpoke | Real-time retro and continuous-feedback platform with AI theme detection and sentiment trends. |
| ClickUp | Project-management suite whose AI (Brain) can summarize retro docs and auto-create action tasks. |
| Team O'Clock | Retro, planning-poker, and standup facilitation with AI summaries and icebreakers. |
| Spinach | AI meeting assistant that captures discussion and produces summaries and action items for agile ceremonies. |
| Krazier | AI-assisted retrospective facilitation that clusters feedback and surfaces recurring themes. |

## The prompt I used

```text
You are an experienced agile coach and facilitator. Below are the raw, unedited retrospective
notes and reaction votes from the CareBridge delivery team's Sprint 6 retro (a 2-week sprint).
Summarize them into:
1) Themes under "What went well" and "What didn't go well" (cluster duplicates; keep the team's voice).
2) An overall sentiment read for the sprint, with the signal you based it on.
3) 3-4 concrete, owned action items for the next sprint (each with a single accountable owner from
   the delivery team: Product Owner, Scrum Master, Clinical SME, Frontend Eng, Backend Eng,
   Data/Platform Eng, QA/Automation Eng, UX Designer, DevOps/SRE).
Be specific to what the notes actually say; do not invent items that aren't supported by the notes.

[Raw notes]
- Audit-trail middleware (CB-9) shipped and is logging every READ/WRITE - compliance is thrilled (+6 votes)
- Task board (CB-5) demoed well; Clinical SME said it "finally looks like how we actually work" (+5)
- Pairing on the RBAC model paid off - far fewer rework cycles than Sprint 5 (+4)
- Audit logging added latency on patient-list load; QA flagged it late, almost slipped to the demo (-5)
- Two stories carried over because FHIR import (CB-15) was blocked waiting on pilot-site export creds (-4)
- Standups drifted long again; several people felt status-report-y rather than blocker-focused (-3)
- Staging environment was flaky midweek; lost ~half a day (-3)
- Great cross-functional energy; UX + Backend unblocked each other fast on the board (+3)
```

## AI-generated output

**CareBridge — Sprint 6 Retrospective (AI-synthesized)**

### What went well
- **Compliance milestone landed.** The HIPAA audit-trail middleware (CB-9) is live and logging every READ/WRITE — the team's most-upvoted item and a direct hit on OKR-3 readiness.
- **The board feels right to clinicians.** The Kanban task board (CB-5) demoed well; the Clinical SME's "finally looks like how we actually work" was a strong validation signal.
- **Pairing reduced rework.** Pairing on the RBAC model cut rework cycles sharply versus Sprint 5, and cross-functional unblocking (UX ↔ Backend) was fast.

### What didn't go well
- **Performance regression caught late.** Audit logging added latency to patient-list load and QA flagged it close to the demo — a near-miss that points to missing performance checks in the definition of done.
- **External dependency stalled FHIR import.** Two stories (CB-15) carried over, blocked on pilot-site export credentials — an avoidable, foreseeable external dependency.
- **Process friction.** Standups drifted long and status-report-y, and a flaky staging environment cost roughly half a day.

### Sentiment read
**Net positive, with clear operational friction.** Reaction votes skew positive on outcomes (audit trail +6, board +5, pairing +4), and the strongest negatives are *process/environment* (latency miss −5, FHIR block −4), not morale or team dynamics. Read: the team is proud of what shipped but frustrated by avoidable drag. Trajectory is good if the friction items are addressed; ignoring them risks eroding the positive energy next sprint.

### Action items

| # | Action | Owner | Why |
|---|--------|-------|-----|
| 1 | Add a patient-list load-time performance check to the Definition of Done and wire it into CI so audit-related latency is caught before demo. | QA/Automation Engineer | Prevents a repeat of the near-miss latency regression. |
| 2 | Profile and fix the audit-logging latency on patient-list load; target restoring pre-CB-9 load time. | Backend Engineer | Protects the daily-use clinical surface from the compliance feature's cost. |
| 3 | Escalate the pilot-site FHIR export-credentials request and set a hard date; do not pull CB-15 back into a sprint until creds are confirmed. | Product Owner | Removes the external blocker that caused two carryovers. |
| 4 | Run timeboxed standups (move detailed status to the board) and stabilize staging (root-cause the midweek flakiness). | Scrum Master / DevOps-SRE | Recovers the half-day lost and refocuses standups on blockers. |

## PM judgment applied

- **Kept the sentiment framing, sharpened the read.** I agreed the sprint was net-positive but explicitly told the team the negatives were *process, not people* — that distinction changes how we act on them, and the AI's vote-based reasoning supported it.
- **Assigned single owners.** The AI's draft left action 4 shared; I kept it dual-owned (Scrum Master for standups, DevOps/SRE for staging) but made each owner's slice explicit so nothing is "everyone's job."
- **Made action 3 a gate, not a task.** I reinforced that CB-15 stays out of the sprint until credentials land — turning a recurring carryover into a pull-condition, which matches how I re-ranked CB-15 in the prioritization artifact.
- **Verified nothing was invented.** I checked every theme and action against the raw notes; the AI added no items that the team didn't actually raise, which is the bar for trusting an AI-summarized retro.

---

_Reusable prompt: [prompt-library](../prompts/prompt-library.md) · Source technique: AI-Powered Agile workbook §1.4._
