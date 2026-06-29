from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..core.db import get_db
from ..models import CarePlan, Patient, Task
from ..schemas import CarePlanCreate, CarePlanOut, TaskOut

router = APIRouter(prefix="/api/care-plans", tags=["care-plans"])


@router.get("", response_model=list[CarePlanOut])
def list_care_plans(db: Session = Depends(get_db)):
    return db.query(CarePlan).order_by(CarePlan.id).all()


@router.post("", response_model=CarePlanOut, status_code=201)
def create_care_plan(payload: CarePlanCreate, db: Session = Depends(get_db)):
    if not db.get(Patient, payload.patient_id):
        raise HTTPException(404, "Patient not found")
    plan = CarePlan(**payload.model_dump())
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return plan


@router.get("/{plan_id}/tasks", response_model=list[TaskOut])
def list_care_plan_tasks(plan_id: int, db: Session = Depends(get_db)):
    if not db.get(CarePlan, plan_id):
        raise HTTPException(404, "Care plan not found")
    return db.query(Task).filter(Task.care_plan_id == plan_id).order_by(Task.id).all()
