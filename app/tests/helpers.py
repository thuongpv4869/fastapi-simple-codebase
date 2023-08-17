from contextlib import contextmanager

from starlette.testclient import TestClient

from app.services.token import create_access_token


@contextmanager
def rollback_transaction(session):
    # rollback all after finish a test
    try:
        yield session.begin_nested()
    finally:
        session.rollback()


def login_client(client: TestClient, user):
    access_token = create_access_token(
        {
            "user_id": user.id,
            "email": user.email,
        }
    )
    client.headers["Authorization"] = f"Bearer {access_token}"
    return client


def logout_client(client: TestClient):
    client.headers.pop("Authorization", None)


@contextmanager
def ensure_logout_client(client: TestClient, user):
    # rollback all after finish a test
    try:
        yield login_client(client, user)
    finally:
        logout_client(client)
