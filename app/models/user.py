from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base
from .mixins import TimestampMixin


class User(TimestampMixin, Base):
    __tablename__ = "user"  # noqa

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    full_name: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    phone: Mapped[str] = mapped_column(unique=True, index=True)
    disabled: Mapped[bool] = mapped_column(default=False)
    password: Mapped[str] = mapped_column()


class UserProfile(TimestampMixin, Base):
    __tablename__ = "user_profile"  # noqa
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="user_profile")
    avatar_path: Mapped[Optional[str]]
