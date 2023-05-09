from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func


class TimestampMixin:
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(),
                                               server_onupdate=func.now(), nullable=False)
