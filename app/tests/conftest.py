from unittest.mock import patch

import pytest
from sqlalchemy import create_engine, make_url
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.orm import sessionmaker, scoped_session
from starlette.testclient import TestClient

from app.config import settings
from app.db.base import Base

from app.main import app
from app.tests.fixtures import *


@pytest.fixture(scope="session")
def db_connection():
    db_url = make_url(settings.SQLALCHEMY_DATABASE_URL)

    engine = create_engine(db_url, echo=True)

    # create db if not exists
    if not database_exists(engine.url):
        create_database(engine.url)

    # create connection
    with engine.connect() as conn:

        # create tables
        Base.metadata.create_all(engine)

        # return connection
        yield conn

    # drop db
    drop_database(engine.url)


@pytest.fixture()
def db(db_connection):
    session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=db_connection)
    )
    try:
        yield session
    finally:
        session.close()


@pytest.fixture()
def db_tran(db_connection):
    with db_connection.begin():
        session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=db_connection)
        )
        try:
            yield session
        finally:
            session.close()


@pytest.fixture(scope="session")
def client(db_connection):
    with patch("app.api.deps.get_db", db_tran):
        return TestClient(app)
