from sqlalchemy import (
    Column,
    Integer,
    Float,
    DateTime,
    ForeignKey,
    JSON
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.base import Base


class JobMatch(Base):
    __tablename__ = "job_matches"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    resume_id = Column(
        Integer,
        ForeignKey("resumes.id"),
        nullable=False
    )

    job_id = Column(
        Integer,
        ForeignKey("jobs.id"),
        nullable=False
    )

    match_score = Column(
        Float,
        nullable=False
    )

    strengths = Column(
        JSON,
        nullable=False
    )

    missing_skills = Column(
        JSON,
        nullable=False
    )

    recommendations = Column(
        JSON,
        nullable=False
    )

    summary = Column(
        JSON,
        nullable=True
    )

    ai_response = Column(
        JSON,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    resume = relationship(
        "Resume",
        back_populates="job_matches"
    )

    job = relationship(
        "Job",
        back_populates="job_matches"
    )

    interviews = relationship(
    "Interview",
    back_populates="job_match",
    cascade="all, delete-orphan"
)
    
    cover_letters = relationship(
    "CoverLetter",
    back_populates="job_match",
    cascade="all, delete-orphan"
)