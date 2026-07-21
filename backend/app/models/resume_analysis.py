from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    JSON,
    String,
    DateTime
)
from sqlalchemy.orm import relationship

from app.database.base import Base


class ResumeAnalysis(Base):
    __tablename__ = "resume_analysis"

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

    analysis = Column(
        JSON,
        nullable=False
    )

    status = Column(
        String(30),
        default="COMPLETED",
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    resume = relationship(
        "Resume",
        back_populates="analysis"
    )