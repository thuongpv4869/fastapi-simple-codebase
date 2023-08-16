import pathlib
import os

from pydantic import BaseSettings
from dotenv import load_dotenv

APP_DIR = pathlib.Path(__file__).parent.resolve()

ROOT_DIR = APP_DIR.parent.resolve()

load_dotenv(os.getenv("ENV_FILE", f"{APP_DIR}/.env"))


class Settings(BaseSettings):
    DEBUG = True
    PROJECT_NAME = os.environ["PROJECT_NAME"]
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URL: str = os.environ["SQLALCHEMY_DATABASE_URL"]
    BACKEND_CORS_ORIGINS = os.environ["BACKEND_CORS_ORIGINS"]

    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"])
    SECRET_KEY = os.environ["SECRET_KEY"]
    MEDIA_DIR: str = "media"
    STATIC_DIR: str = "static"
    AWS_S3_DEFAULT_BUCKET: str = os.environ.get("AWS_S3_DEFAULT_BUCKET")


settings = Settings()
