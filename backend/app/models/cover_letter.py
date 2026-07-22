from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime,
    Text
)

from sqlalchemy.orm import relationship

from app.database.database import Base


class CoverLetter(Base):
    __tablename__ = "cover_letters"

    id = Column(Integer, primary_key=True, index=True)

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

    content = Column(Text, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="cover_letters"
    )

    resume = relationship(
        "Resume",
        back_populates="cover_letters"
    )

    job = relationship(
        "Job",
        back_populates="cover_letters"
    )

    job_match = relationship(
        "JobMatch",
        back_populates="cover_letters"
    )