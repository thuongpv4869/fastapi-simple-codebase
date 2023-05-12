from sqlalchemy.orm import Mapped, mapped_column

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
