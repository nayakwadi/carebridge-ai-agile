"""SQLAlchemy engine/session wiring. Works against PostgreSQL (Docker) or SQLite (tests)."""
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool

from .config import settings

connect_args: dict = {}
engine_kwargs: dict = {"pool_pre_ping": True}

if settings.database_url.startswith("sqlite"):
    # In-memory SQLite needs a single shared connection across threads (tests/TestClient).
    connect_args = {"check_same_thread": False}
    engine_kwargs = {"poolclass": StaticPool}

engine = create_engine(settings.database_url, connect_args=connect_args, **engine_kwargs)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def get_db() -> Generator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
