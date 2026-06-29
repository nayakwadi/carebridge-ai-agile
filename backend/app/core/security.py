"""JWT issue/verify helpers.

DEMONSTRATION STUB. A real deployment would integrate an identity provider
(OIDC / SMART-on-FHIR for healthcare) rather than a shared demo password.
"""
from datetime import UTC, datetime, timedelta

import jwt

from .config import settings

ALGORITHM = "HS256"


def create_access_token(subject: str) -> str:
    expire = datetime.now(UTC) + timedelta(minutes=settings.jwt_expire_minutes)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, settings.jwt_secret, algorithm=ALGORITHM)


def decode_token(token: str) -> str | None:
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[ALGORITHM])
        return payload.get("sub")
    except jwt.PyJWTError:
        return None
