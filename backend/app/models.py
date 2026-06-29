"""SQLAlchemy ORM models. Mirror database/init.sql exactly (single source of truth)."""
from sqlalchemy import (
    CheckConstraint,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import relationship

from .core.db import Base


class CareTeamMember(Base):
    __tablename__ = "care_team_members"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(120), nullable=False)
    role = Column(String(60), nullable=False)
    email = Column(String(160), nullable=False, unique=True)
    specialty = Column(String(120))
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    mrn = Column(String(20), nullable=False, unique=True)
    full_name = Column(String(120), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    primary_condition = Column(String(160), nullable=False)
    risk_level = Column(String(10), nullable=False, default="medium")
    status = Column(String(20), nullable=False, default="active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    care_plans = relationship("CarePlan", back_populates="patient", cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint("risk_level IN ('low','medium','high')", name="ck_patient_risk"),
        CheckConstraint(
            "status IN ('active','discharged','transferred')", name="ck_patient_status"
        ),
    )


class CarePlan(Base):
    __tablename__ = "care_plans"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(160), nullable=False)
    goal = Column(Text)
    status = Column(String(20), nullable=False, default="active")
    start_date = Column(Date)
    target_date = Column(Date)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    patient = relationship("Patient", back_populates="care_plans")
    tasks = relationship("Task", back_populates="care_plan", cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint(
            "status IN ('draft','active','on_hold','completed')", name="ck_plan_status"
        ),
    )


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    care_plan_id = Column(
        Integer, ForeignKey("care_plans.id", ondelete="CASCADE"), nullable=False
    )
    title = Column(String(200), nullable=False)
    description = Column(Text)
    status = Column(String(20), nullable=False, default="todo")
    priority = Column(String(10), nullable=False, default="medium")
    assignee_id = Column(Integer, ForeignKey("care_team_members.id", ondelete="SET NULL"))
    due_date = Column(Date)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    care_plan = relationship("CarePlan", back_populates="tasks")
    assignee = relationship("CareTeamMember")

    __table_args__ = (
        CheckConstraint(
            "status IN ('todo','in_progress','blocked','done')", name="ck_task_status"
        ),
        CheckConstraint(
            "priority IN ('low','medium','high','urgent')", name="ck_task_priority"
        ),
    )


class AuditLog(Base):
    __tablename__ = "audit_log"

    id = Column(Integer, primary_key=True)
    occurred_at = Column(DateTime(timezone=True), server_default=func.now())
    actor = Column(String(160))
    action = Column(String(20), nullable=False)
    method = Column(String(10), nullable=False)
    path = Column(String(300), nullable=False)
    status_code = Column(Integer, nullable=False)
    client_ip = Column(String(64))
