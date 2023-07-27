from sqlalchemy.orm import Session

from app import models
from app.services.common import get_password_hash


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, email, full_name, phone, plain_pass):
    user = models.User(
        email=email,
        full_name=full_name,
        phone=phone,
        password=get_password_hash(plain_pass)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def create_admin_user(db: Session, email, plain_pass):
    return create_user(db, email, full_name="admin", phone="099xxxxxx", plain_pass=plain_pass)