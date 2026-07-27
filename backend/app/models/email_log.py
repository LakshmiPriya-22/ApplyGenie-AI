from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text
)

from sqlalchemy.orm import relationship

from app.database.database import Base


class EmailLog(Base):
    __tablename__ = "email_logs"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    application_id = Column(
        Integer,
        ForeignKey("applications.id", ondelete="CASCADE"),
        nullable=False
    )

    recipient_email = Column(
        String(255),
        nullable=False
    )

    subject = Column(
        String(255),
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False,
        default="Pending"
    )

    error_message = Column(
        Text,
        nullable=True
    )

    sent_at = Column(
        DateTime,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="email_logs"
    )

    application = relationship(
        "Application",
        back_populates="email_logs"
    )