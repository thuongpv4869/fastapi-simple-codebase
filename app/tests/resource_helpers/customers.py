from app import schemas
from app.services import crud_customer
from app.tests.resource_helpers import fake


def create_customer_db(db):
    customer_input = schemas.CustomerCreate(
        full_name=fake.name(), email=fake.email(), phone=fake.phone_number(), address=fake.address()
    )
    customer_db = crud_customer.create_customer(db, customer_input)
    return customer_db
