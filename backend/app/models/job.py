from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.base import Base


class Job(Base):
    __tablename__ = "jobs"

    # ---------------------------------------
    # Primary Key
    # ---------------------------------------
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # ---------------------------------------
    # Job Details
    # ---------------------------------------
    title = Column(
        String,
        nullable=False
    )

    company = Column(
        String,
        nullable=False
    )

    location = Column(
        String,
        nullable=False
    )

    employment_type = Column(
        String,
        nullable=False
    )

    experience_level = Column(
        String,
        nullable=False
    )

    salary = Column(
        String,
        nullable=True
    )

    description = Column(
        Text,
        nullable=False
    )

    requirements = Column(
        Text,
        nullable=False
    )

    skills = Column(
        Text,
        nullable=True
    )

    # ---------------------------------------
    # Ownership
    # External jobs can have no owner
    # ---------------------------------------
    posted_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    # ---------------------------------------
    # Audit Fields
    # ---------------------------------------
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    # ---------------------------------------
    # Relationships
    # ---------------------------------------
    user = relationship(
        "User",
        back_populates="jobs",
        lazy="selectin"
    )

    job_matches = relationship(
        "JobMatch",
        back_populates="job",
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    applications = relationship(
        "Application",
        back_populates="job",
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    cover_letters = relationship(
        "CoverLetter",
        back_populates="job",
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    interviews = relationship(
        "Interview",
        back_populates="job",
        cascade="all, delete-orphan",
        lazy="selectin"
    )