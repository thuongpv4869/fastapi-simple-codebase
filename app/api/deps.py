from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app import services
from app.config import settings
from app.db.session import SessionLocal


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/token-form")


def get_current_user(db=Depends(get_db), token=Depends(oauth2_scheme)):
    return services.token.get_current_user(db, token)

