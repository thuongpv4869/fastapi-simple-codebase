import io

from app.config import settings
from app.tests.helpers import rollback_transaction, ensure_logout_client
from app.tests.resource_helpers.user import create_user_db

api_v1_prefix = settings.API_V1_STR


def test_upload_user_avatar(client, db):
    with rollback_transaction(db):
        user = create_user_db(db)

        with ensure_logout_client(client, user) as logged_in_client:
            route = f"{api_v1_prefix}/users/avatar"

            response = logged_in_client.post(route, files={"file": ("a.jpg", io.BytesIO(b"abcdef"), "image/jpg")})

            assert response.status_code == 200
            assert response.json()["avatar_url"]
