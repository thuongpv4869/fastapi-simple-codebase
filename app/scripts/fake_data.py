import logging

from app import models
from app.db.session import SessionLocal

from faker import Faker

from app.services.token import get_password_hash

fake = Faker()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fake_customers(db):
    customers = []
    for x in range(5):
        customers.append(
            models.Customer(
                full_name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address()
            )
        )
    db.bulk_save_objects(customers)
    db.commit()


def create_admin_user(db):

    plain_pass = "changeme"
    user = models.User(
        email="admin",
        full_name="admin",
        phone="123456789",
        password=get_password_hash(plain_pass)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    print(f"user admin has been created: {user.email}/{plain_pass}")
    return user


def main() -> None:
    logger.info("Creating fake data")
    db = SessionLocal()
    create_admin_user(db)
    fake_customers(db)
    logger.info("fake data created")


if __name__ == "__main__":
    main()
