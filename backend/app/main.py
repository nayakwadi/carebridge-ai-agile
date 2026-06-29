"""CareBridge API — application tier entry point."""
import time
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from .core import cache
from .core.audit import AuditMiddleware
from .core.config import settings
from .core.db import Base, SessionLocal, engine, get_db
from .models import CarePlan, Patient, Task
from .routers import auth, care_plans, patients, tasks
from .schemas import Stats
from .seed import seed


def _wait_for_db(retries: int = 10, delay: float = 2.0) -> None:
    """Postgres may still be starting when the API boots; retry briefly."""
    for attempt in range(retries):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(delay)


@asynccontextmanager
async def lifespan(app: FastAPI):
    _wait_for_db()
    Base.metadata.create_all(bind=engine)  # no-op when init.sql already created the schema
    db = SessionLocal()
    try:
        seed(db)  # no-op when seed.sql already populated postgres
    finally:
        db.close()
    yield


app = FastAPI(
    title="CareBridge API",
    version="1.0.0",
    description="AI-assisted patient care-coordination platform — application tier.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(AuditMiddleware)

app.include_router(patients.router)
app.include_router(care_plans.router)
app.include_router(tasks.router)
app.include_router(auth.router)


@app.get("/health", tags=["meta"])
def health():
    return {"status": "ok", "cache": cache.available()}


@app.get("/api/stats", response_model=Stats, tags=["meta"])
def stats(db: Session = Depends(get_db)):
    cached = cache.get_json("stats")
    if cached:
        return Stats(**cached, cached=True)
    data = {
        "patients": db.query(Patient).count(),
        "care_plans": db.query(CarePlan).count(),
        "open_tasks": db.query(Task).filter(Task.status != "done").count(),
    }
    cache.set_json("stats", data, ttl_seconds=15)
    return Stats(**data, cached=False)
