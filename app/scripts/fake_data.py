import logging

from app import models
from app.db.session import SessionLocal

from faker import Faker
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


def init() -> None:
    db = SessionLocal()
    fake_customers(db)


def main() -> None:
    logger.info("Creating fake data")
    init()
    logger.info("fake data created")


if __name__ == "__main__":
    main()
