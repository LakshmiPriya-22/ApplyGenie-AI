from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
    JSON,
    Text,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.base import Base


class Interview(Base):

    __tablename__ = "interviews"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    resume_id = Column(
        Integer,
        ForeignKey("resumes.id", ondelete="CASCADE"),
        nullable=False
    )

    job_id = Column(
        Integer,
        ForeignKey("jobs.id", ondelete="CASCADE"),
        nullable=False
    )

    job_match_id = Column(
        Integer,
        ForeignKey("job_matches.id", ondelete="CASCADE"),
        nullable=False
    )

    interview_type = Column(
        String,
        nullable=False,
        default="Technical + HR"
    )

    difficulty = Column(
        String,
        nullable=False,
        default="Medium"
    )

    questions = Column(
        JSON,
        nullable=False
    )

    answers = Column(
        JSON,
        nullable=True
    )

    feedback = Column(
        JSON,
        nullable=True
    )

    tips = Column(
        JSON,
        nullable=True
    )

    roadmap = Column(
        JSON,
        nullable=True
    )

    summary = Column(
        Text,
        nullable=True
    )

    score = Column(
        Float,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # -------------------------
    # Relationships
    # -------------------------

    user = relationship(
        "User",
        back_populates="interviews"
    )

    resume = relationship(
        "Resume",
        back_populates="interviews"
    )

    job = relationship(
        "Job",
        back_populates="interviews"
    )

    job_match = relationship(
        "JobMatch",
        back_populates="interviews"
    )