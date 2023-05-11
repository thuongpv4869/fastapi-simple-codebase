from fastapi import Depends
from sqlalchemy.orm import Session

from app import schemas, models
from app.api import deps

from fastapi import APIRouter

router = APIRouter()


@router.post("/me", response_model=schemas.UserMe)
async def get_me(current_user: models.User = Depends(deps.get_current_user)):
    return current_user
