from app import models
from app.config import settings
from app.tests.fixtures import fake
from app.tests.helpers import rollback_transaction

api_v1_prefix = settings.API_V1_STR


def test_read_customer(client, customer_db, db):
    with rollback_transaction(db):
        route = f"{api_v1_prefix}/customers/{customer_db.id}"
        response = client.get(route)
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
