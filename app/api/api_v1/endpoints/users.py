import os

from fastapi import APIRouter, Depends, UploadFile, Request

from app import schemas, models
from app.api import deps
from app.services.storage import storage_service

router = APIRouter()


@router.post("/me", response_model=schemas.UserMe)
async def get_me(current_user: models.User = Depends(deps.get_current_user)):
    return current_user


@router.post("/avatar", response_model=schemas.UserAvatar)
async def upload_avatar(file: UploadFile, request: Request, current_user: models.User = Depends(deps.get_current_user)):
    filename, file_extension = os.path.splitext(file.filename)
    dest = f"user/{current_user.id}/avatar{file_extension}"

    avatar_path = storage_service.upload(file, dest)
    if "http" not in avatar_path:
        avatar_path = f"{request.base_url}{avatar_path}"
    return schemas.UserAvatar(avatar_url=avatar_path)
