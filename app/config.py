import pathlib

from pydantic import BaseSettings

ROOT_DIR = pathlib.Path(__file__).parent.parent.resolve()


# TODO
# use env file
class Settings(BaseSettings):
    PROJECT_NAME = "fast api simple"
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URL: str = f"sqlite:///{ROOT_DIR}/sql_app.db"
    BACKEND_CORS_ORIGINS = ["http://localhost", "http://localhost:8000"]


settings = Settings()
