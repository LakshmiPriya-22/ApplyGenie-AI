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

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

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

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    posted_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="jobs"
    )

    job_matches = relationship(
    "JobMatch",
    back_populates="job",
    cascade="all, delete-orphan"
)
    
    applications = relationship(
    "Application",
    back_populates="job",
    cascade="all, delete-orphan"
)