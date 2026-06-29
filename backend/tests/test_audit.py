from app.core.db import SessionLocal
from app.models import AuditLog


def test_request_is_written_to_audit_log(client):
    client.get("/api/patients")
    db = SessionLocal()
    try:
        rows = db.query(AuditLog).filter(AuditLog.path == "/api/patients").all()
        assert rows, "expected an audit entry for the PHI request"
        assert rows[-1].action == "READ"
        assert rows[-1].method == "GET"
    finally:
        db.close()


def test_write_is_classified_as_write(client):
    client.post(
        "/api/patients",
        json={
            "mrn": "MRN-AUDIT1",
            "full_name": "Audit Subject",
            "date_of_birth": "1980-05-05",
            "primary_condition": "Observation",
        },
    )
    db = SessionLocal()
    try:
        row = (
            db.query(AuditLog)
            .filter(AuditLog.path == "/api/patients", AuditLog.action == "WRITE")
            .first()
        )
        assert row is not None
    finally:
        db.close()
