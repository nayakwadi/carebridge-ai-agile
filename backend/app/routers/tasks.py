from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..core.db import get_db
from ..models import CarePlan, Task
from ..schemas import TaskCreate, TaskOut, TaskUpdate

router = APIRouter(prefix="/api/tasks", tags=["tasks"])

VALID_STATUS = {"todo", "in_progress", "blocked", "done"}


@router.get("", response_model=list[TaskOut])
def list_tasks(db: Session = Depends(get_db)):
    return db.query(Task).order_by(Task.id).all()


@router.post("", response_model=TaskOut, status_code=201)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)):
    if not db.get(CarePlan, payload.care_plan_id):
        raise HTTPException(404, "Care plan not found")
    task = Task(**payload.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.patch("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db)):
    """Used by the Kanban board to move a task across columns or reassign it."""
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(404, "Task not found")
    if payload.status is not None and payload.status not in VALID_STATUS:
        raise HTTPException(422, f"Invalid status. Allowed: {sorted(VALID_STATUS)}")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task
