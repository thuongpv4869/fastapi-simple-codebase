import os
import shutil

from fastapi import UploadFile
from app.config import settings, APP_DIR
from pathlib import Path


def upload_local(file: UploadFile, dest):
    dest_path = f"{settings.MEDIA_DIR}/{dest}"
    full_path = f"{APP_DIR}/{dest_path}"
    Path(full_path).parent.mkdir(exist_ok=True, parents=True)
    with open(full_path, "wb") as dest_f:
        shutil.copyfileobj(file.file, dest_f)

    return dest_path


def upload_cloud(file: UploadFile, dest):
    from .aws_s3 import bucket, boto3

    dest_path = f"{settings.MEDIA_DIR}/{dest}"
    bucket.put_object(Body=file.file, Key=dest_path)

    _, file_extension = os.path.splitext(dest_path)
    url = boto3.client("s3").generate_presigned_url(
        ClientMethod="get_object",
        Params={
            "Bucket": bucket.name,
            "Key": dest_path,
            "ResponseContentType": f"image/{file_extension.split('.')[-1]}",
        },
        ExpiresIn=3600,
    )
    return url


class StorageService:
    def __init__(self, provider_type="LOCAL"):
        self.provider_type = provider_type

    def upload(self, file: UploadFile, dest):
        if self.provider_type == "CLOUD":
            return upload_cloud(file, dest)

        return upload_local(file, dest)


storage_service = StorageService(provider_type=settings.DEBUG and "LOCAL" or "CLOUD")
