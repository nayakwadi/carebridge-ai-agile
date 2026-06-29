"""HIPAA-style audit middleware.

Every request to a PHI-bearing API path is appended to the audit_log table with
who (actor), what (READ/WRITE + method/path), and the outcome (status code).
This is the kind of immutable access trail a healthcare regulator expects.
"""
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from ..models import AuditLog
from .db import SessionLocal
from .security import decode_token

AUDITED_PREFIX = "/api"
READ_METHODS = {"GET", "HEAD", "OPTIONS"}


class AuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        if request.url.path.startswith(AUDITED_PREFIX):
            actor = "anonymous"
            auth = request.headers.get("authorization", "")
            if auth.lower().startswith("bearer "):
                actor = decode_token(auth[7:]) or "anonymous"

            db = SessionLocal()
            try:
                db.add(
                    AuditLog(
                        actor=actor,
                        action="READ" if request.method in READ_METHODS else "WRITE",
                        method=request.method,
                        path=request.url.path,
                        status_code=response.status_code,
                        client_ip=request.client.host if request.client else None,
                    )
                )
                db.commit()
            except Exception:
                db.rollback()
            finally:
                db.close()

        return response
