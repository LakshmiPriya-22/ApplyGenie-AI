from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import Text
from app.database.base import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    filepath = Column(String, nullable=False)
    extracted_text = Column(Text, nullable=True)

    uploaded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    user = relationship(
        "User",
        back_populates="resumes"
    )
    analysis = relationship(
    "ResumeAnalysis",
    back_populates="resume",
    uselist=False
)
    job_matches = relationship(
    "JobMatch",
    back_populates="resume",
    cascade="all, delete-orphan"
)
    applications = relationship(
    "Application",
    back_populates="resume",
    cascade="all, delete-orphan"
)
    
    interviews = relationship(
    "Interview",
    back_populates="resume",
    cascade="all, delete-orphan"
)
    cover_letters = relationship(
    "CoverLetter",
    back_populates="resume",
    cascade="all, delete-orphan"
)