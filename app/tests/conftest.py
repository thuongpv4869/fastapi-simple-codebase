from unittest.mock import patch

import pytest  # noqa
from sqlalchemy import create_engine, make_url
from sqlalchemy_utils import functions as db_helpers
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from app.config import settings
from app.db.base import Base

from app.tests.fixtures import *  # noqa


@pytest.fixture(scope="session")
def db():
    db_url = make_url(settings.SQLALCHEMY_DATABASE_URL)
    db_url.set("database", "simple_api_test")

    engine = create_engine(db_url, echo=True)

    # create new db test.sh if not exists
    if not db_helpers.database_exists(engine.url):
        db_helpers.create_database(engine.url)

    # create tables
    Base.metadata.create_all(engine)

    # return session
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    with session:
        yield session

    # drop db
    db_helpers.drop_database(engine.url)


@pytest.fixture(scope="session")
def client(db):
    def get_db():
        yield db

    with patch("app.api.deps.get_db", get_db):
        from app.main import app

        with TestClient(app) as client:
            yield client
