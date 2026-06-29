"""Idempotent ORM seeder.

Used for SQLite/test/bare-metal runs. In Docker the postgres container is already
seeded by database/seed.sql, so this seeder sees existing rows and does nothing.
"""
from datetime import date

from sqlalchemy.orm import Session

from .models import CarePlan, CareTeamMember, Patient, Task


def seed(db: Session) -> None:
    if db.query(Patient).first():
        return  # already seeded

    team = [
        CareTeamMember(full_name="Dr. Amara Okafor", role="Physician",
                       email="a.okafor@carebridge.example", specialty="Internal Medicine"),
        CareTeamMember(full_name="Liam Chen", role="Nurse",
                       email="l.chen@carebridge.example", specialty="Med-Surg"),
        CareTeamMember(full_name="Priya Nair", role="Care Coordinator",
                       email="p.nair@carebridge.example", specialty="Transitions of Care"),
        CareTeamMember(full_name="Marcus Webb", role="Social Worker",
                       email="m.webb@carebridge.example", specialty="Behavioral Health"),
        CareTeamMember(full_name="Dr. Sofia Rossi", role="Pharmacist",
                       email="s.rossi@carebridge.example", specialty="Medication Reconciliation"),
    ]
    db.add_all(team)
    db.flush()
    by_name = {m.full_name: m for m in team}

    eleanor = Patient(mrn="MRN-100247", full_name="Eleanor Whitfield",
                      date_of_birth=date(1948, 3, 12),
                      primary_condition="Congestive Heart Failure", risk_level="high")
    theodore = Patient(mrn="MRN-100311", full_name="Theodore Banks",
                       date_of_birth=date(1955, 9, 30),
                       primary_condition="Type 2 Diabetes", risk_level="medium")
    db.add_all([
        eleanor, theodore,
        Patient(mrn="MRN-100422", full_name="Rosa Delgado", date_of_birth=date(1967, 1, 22),
                primary_condition="COPD", risk_level="high"),
        Patient(mrn="MRN-100538", full_name="Henry Osei", date_of_birth=date(1972, 7, 5),
                primary_condition="Post-Op Hip Replacement", risk_level="medium"),
        Patient(mrn="MRN-100644", full_name="Grace Lindqvist", date_of_birth=date(1989, 11, 18),
                primary_condition="Hypertension", risk_level="low"),
    ])
    db.flush()

    chf = CarePlan(patient_id=eleanor.id, title="30-Day CHF Readmission Prevention",
                   goal="Keep patient stable at home; avoid readmission within 30 days.",
                   status="active", start_date=date(2026, 6, 1), target_date=date(2026, 7, 1))
    dm = CarePlan(patient_id=theodore.id, title="Diabetes Self-Management Ramp-Up",
                  goal="Achieve HbA1c < 7.5 and confident self-administered insulin in 8 weeks.",
                  status="active", start_date=date(2026, 5, 20), target_date=date(2026, 7, 15))
    db.add_all([chf, dm])
    db.flush()

    db.add_all([
        Task(care_plan_id=chf.id, title="Schedule 48-hour post-discharge follow-up call",
             status="done", priority="high", assignee_id=by_name["Liam Chen"].id,
             due_date=date(2026, 6, 3)),
        Task(care_plan_id=chf.id, title="Medication reconciliation",
             status="in_progress", priority="urgent", assignee_id=by_name["Dr. Sofia Rossi"].id,
             due_date=date(2026, 6, 5)),
        Task(care_plan_id=chf.id, title="Arrange home scale + daily weight log",
             status="todo", priority="medium", assignee_id=by_name["Priya Nair"].id,
             due_date=date(2026, 6, 8)),
        Task(care_plan_id=chf.id, title="Confirm cardiology appointment",
             status="blocked", priority="high", assignee_id=by_name["Priya Nair"].id,
             due_date=date(2026, 6, 9)),
        Task(care_plan_id=dm.id, title="Insulin self-administration teach-back",
             status="in_progress", priority="high", assignee_id=by_name["Liam Chen"].id,
             due_date=date(2026, 6, 12)),
        Task(care_plan_id=dm.id, title="Dietitian referral",
             status="todo", priority="medium", assignee_id=by_name["Marcus Webb"].id,
             due_date=date(2026, 6, 18)),
        Task(care_plan_id=dm.id, title="Baseline HbA1c lab draw",
             status="done", priority="medium", assignee_id=by_name["Dr. Amara Okafor"].id,
             due_date=date(2026, 5, 22)),
    ])
    db.commit()
