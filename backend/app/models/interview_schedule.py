from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.base import Base


class InterviewSchedule(Base):

    __tablename__ = "interview_schedules"

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

    company = Column(String, nullable=False)

    job_title = Column(String, nullable=False)

    interviewer_name = Column(String)

    mode = Column(String)        # Online / Offline

    meeting_link = Column(String)

    location = Column(String)

    scheduled_at = Column(DateTime, nullable=False)

    status = Column(
        String,
        default="Scheduled"
    )

    notes = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    user = relationship("User")
    application = relationship("Application")