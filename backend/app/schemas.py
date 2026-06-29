"""Pydantic request/response schemas."""
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field


class CareTeamMemberOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    full_name: str
    role: str
    email: str
    specialty: str | None = None


class PatientBase(BaseModel):
    mrn: str = Field(..., max_length=20)
    full_name: str
    date_of_birth: date
    primary_condition: str
    risk_level: str = "medium"
    status: str = "active"


class PatientCreate(PatientBase):
    pass


class PatientOut(PatientBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime | None = None


class CarePlanBase(BaseModel):
    title: str
    goal: str | None = None
    status: str = "active"
    start_date: date | None = None
    target_date: date | None = None


class CarePlanCreate(CarePlanBase):
    patient_id: int


class CarePlanOut(CarePlanBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    patient_id: int


class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: str = "todo"
    priority: str = "medium"
    assignee_id: int | None = None
    due_date: date | None = None


class TaskCreate(TaskBase):
    care_plan_id: int


class TaskUpdate(BaseModel):
    """Partial update — used by the Kanban board to move a task between columns."""
    status: str | None = None
    priority: str | None = None
    assignee_id: int | None = None


class TaskOut(TaskBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    care_plan_id: int


class Stats(BaseModel):
    patients: int
    care_plans: int
    open_tasks: int
    cached: bool


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
