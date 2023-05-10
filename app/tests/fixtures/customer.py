import pytest
from faker import Faker
from app import schemas
from app.services import crud_customer

fake = Faker()


@pytest.fixture()
def customer_db(db):
    customer_input = schemas.CustomerCreate(
            full_name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address()
        )
    customer_db = crud_customer.create_customer(db, customer_input)
    assert customer_db.id
    assert customer_db.email == customer_db.email
    return customer_db
