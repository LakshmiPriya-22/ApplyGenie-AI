from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    String,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.base import Base


class Settings(Base):

    __tablename__ = "settings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    # -----------------------------------------
    # Notification Preferences
    # -----------------------------------------

    email_notifications = Column(
        Boolean,
        default=True,
        nullable=False
    )

    job_notifications = Column(
        Boolean,
        default=True,
        nullable=False
    )

    interview_notifications = Column(
        Boolean,
        default=True,
        nullable=False
    )

    # -----------------------------------------
    # Appearance
    # -----------------------------------------

    theme = Column(
        String(20),
        default="dark",
        nullable=False
    )

    # -----------------------------------------
    # Timestamps
    # -----------------------------------------

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # -----------------------------------------
    # Relationship
    # -----------------------------------------

    user = relationship(
        "User",
        back_populates="settings"
    )