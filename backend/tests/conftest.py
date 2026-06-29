"""Test configuration: run the whole suite against in-memory SQLite, no Docker needed."""
import os

# Must be set BEFORE importing the app so the engine binds to SQLite.
os.environ["DATABASE_URL"] = "sqlite+pysqlite:///:memory:"
os.environ["REDIS_URL"] = "redis://localhost:6399/0"  # closed port -> cache auto-disables

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from app.core.db import Base, SessionLocal, engine  # noqa: E402
from app.main import app  # noqa: E402
from app.seed import seed  # noqa: E402


@pytest.fixture(scope="session", autouse=True)
def _setup_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed(db)
    finally:
        db.close()
    yield


@pytest.fixture
def client():
    return TestClient(app)
