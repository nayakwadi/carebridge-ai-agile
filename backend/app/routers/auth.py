from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from ..core.security import create_access_token, decode_token
from ..schemas import Token

router = APIRouter(prefix="/api/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/token", auto_error=False)

# DEMO ONLY: any seeded care-team email + the password below authenticates.
DEMO_PASSWORD = "demo"


@router.post("/token", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends()):
    if form.password != DEMO_PASSWORD:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED, "Invalid credentials (demo password is 'demo')"
        )
    return Token(access_token=create_access_token(form.username))


def current_subject(token: str | None = Depends(oauth2_scheme)) -> str:
    subject = decode_token(token) if token else None
    if not subject:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Not authenticated")
    return subject


@router.get("/me")
def whoami(subject: str = Depends(current_subject)):
    return {"subject": subject}
