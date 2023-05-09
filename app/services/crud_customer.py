from sqlalchemy.orm import Session

from app import schemas, models


def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(
        email=customer.email,
        full_name=customer.full_name,
        phone=customer.phone,
        address=customer.address,
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def read_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()


def update_customer(db: Session, customer: schemas.CustomerUpdate, customer_db: models.Customer):
    customer_db.phone = customer.phone
    customer_db.full_name = customer.full_name
    customer_db.address = customer.address

    db.add(customer_db)
    db.commit()
    db.refresh(customer_db)
    return customer_db


def delete_customer(db: Session, customer_db: models.Customer):
    db.delete(customer_db)
    db.commit()
    return customer_db


def list_customer(db: Session):
    customers = db.query(models.Customer).all()
    return customers
