from app import models
from app.config import settings
from app.tests.helpers import rollback_transaction
from app.tests.resource_helpers import fake
from app.tests.resource_helpers.customers import create_customer_db

api_v1_prefix = settings.API_V1_STR


def test_read_customer(client, db):
    with rollback_transaction(db):
        # setup fixtures
        customer_db = create_customer_db(db)

        # execute
        route = f"{api_v1_prefix}/customers/{customer_db.id}"
        response = client.get(route)

        # assert
        assert response.status_code == 200
        assert response.json()["id"] == customer_db.id


def test_create_customer(db, client):
    with rollback_transaction(db):
        payload = dict(full_name=fake.name(), email=fake.email(), phone=fake.phone_number(), address=fake.address())
        url = f"{api_v1_prefix}/customers"

        response = client.post(url, json=payload)

        customer_db = db.query(models.Customer).filter(models.Customer.email == payload["email"]).first()
        assert customer_db
        assert response.json()["email"] == customer_db.email
