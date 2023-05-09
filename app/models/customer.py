from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .mixins import TimestampMixin


class Customer(TimestampMixin, Base):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    full_name: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    phone: Mapped[str] = mapped_column(unique=True, index=True)
    address: Mapped[str] = mapped_column()

    identity_card: Mapped["CustomerIdentityCard"] = relationship(back_populates="customer")


class CustomerIdentityCard(TimestampMixin, Base):
    __tablename__ = "customer_identity_card"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    card_number: Mapped[str] = mapped_column(index=True, nullable=False)
    full_name: Mapped[str] = mapped_column(index=True, nullable=False)
    date_of_birth: Mapped[date] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)
    nationality: Mapped[str] = mapped_column(nullable=False)
    place_of_origin: Mapped[str] = mapped_column(nullable=False)
    place_of_residence: Mapped[str] = mapped_column(nullable=False)
    date_of_expiry: Mapped[date] = mapped_column(nullable=False)
    date_of_issue: Mapped[date] = mapped_column(nullable=False)

    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    customer: Mapped["Customer"] = relationship(back_populates="identity_card")

