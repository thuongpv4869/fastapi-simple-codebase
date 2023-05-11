import pathlib
import os

from pydantic import BaseSettings
from dotenv import load_dotenv

APP_DIR = pathlib.Path(__file__).parent.resolve()

ROOT_DIR = APP_DIR.parent.resolve()

load_dotenv(os.getenv("ENV_FILE", f"{APP_DIR}/.env"))


class Settings(BaseSettings):
    PROJECT_NAME = os.environ["PROJECT_NAME"]
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URL: str = os.environ["SQLALCHEMY_DATABASE_URL"]
    BACKEND_CORS_ORIGINS = os.environ["BACKEND_CORS_ORIGINS"]


settings = Settings()
