import pathlib
import os

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv(os.getenv("ENV_FILE", ".env"))

ROOT_DIR = pathlib.Path(__file__).parent.parent.resolve()


class Settings(BaseSettings):
    PROJECT_NAME = os.environ["PROJECT_NAME"]
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URL: str = os.environ["SQLALCHEMY_DATABASE_URL"]
    BACKEND_CORS_ORIGINS = os.environ["BACKEND_CORS_ORIGINS"]


settings = Settings()
