from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    resumes = relationship(
        "Resume",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    jobs = relationship(
        "Job",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    applications = relationship(
    "Application",
    back_populates="user",
    cascade="all, delete-orphan"
)
    
    interviews = relationship(
    "Interview",
    back_populates="user",
    cascade="all, delete-orphan"
)
    cover_letters = relationship(
    "CoverLetter",
    back_populates="user",
    cascade="all, delete-orphan"
)
    email_logs = relationship(
    "EmailLog",
    back_populates="user",
    cascade="all, delete-orphan"
)
   