import pathlib
import os

from pydantic import BaseSettings
from dotenv import load_dotenv

APP_DIR = pathlib.Path(__file__).parent.resolve()

ROOT_DIR = APP_DIR.parent.resolve()

load_dotenv(os.getenv("ENV_FILE", f"{APP_DIR}/.env"))


def get_default_static_dir():
    static_dir = (APP_DIR / "static").resolve().__str__()
    return static_dir


class Settings(BaseSettings):
    PROJECT_NAME = os.environ["PROJECT_NAME"]
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URL: str = os.environ["SQLALCHEMY_DATABASE_URL"]
    BACKEND_CORS_ORIGINS = os.environ["BACKEND_CORS_ORIGINS"]

    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"])
    SECRET_KEY = os.environ["SECRET_KEY"]
    STATIC_DIR: str = get_default_static_dir()


settings = Settings()
