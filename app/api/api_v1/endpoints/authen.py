from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import schemas
from app import services
from app.api import deps

from fastapi import APIRouter

router = APIRouter()


@router.post("/token", response_model=schemas.TokenData)
def token_create(login_input: schemas.TokenCreate, db: Session = Depends(deps.get_db)):
    user_db = services.crud_user.get_user_by_email(db, login_input.email)
    if not user_db:
        raise HTTPException(status_code=400, detail="email not found")

    if not services.token.verify_password(login_input.password, user_db.password):
        raise HTTPException(status_code=400, detail="Invalid")

    access_token = services.token.create_access_token(
        {
            "user_id": user_db.id,
            "email": user_db.email,
        }
    )

    return dict(access_token=access_token, user_id=user_db.id, email=user_db.email)


@router.post("/token-form", response_model=schemas.TokenData)
def token_form(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(deps.get_db)):
    json_data = schemas.TokenCreate(email=form_data.username, password=form_data.password)
    return token_create(json_data, db)
