from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.base import Base


class Profile(Base):

    __tablename__ = "profiles"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    # -----------------------------
    # Personal Information
    # -----------------------------

    full_name = Column(
        String(100),
        nullable=False
    )

    phone = Column(
        String(20),
        nullable=True
    )

    date_of_birth = Column(
        String(20),
        nullable=True
    )

    gender = Column(
        String(20),
        nullable=True
    )

    # -----------------------------
    # Education
    # -----------------------------

    college = Column(
        String(255),
        nullable=True
    )

    degree = Column(
        String(100),
        nullable=True
    )

    branch = Column(
        String(100),
        nullable=True
    )

    current_year = Column(
        String(30),
        nullable=True
    )

    cgpa = Column(
        Float,
        nullable=True
    )

    # -----------------------------
    # Professional
    # -----------------------------

    headline = Column(
        String(255),
        nullable=True
    )

    bio = Column(
        Text,
        nullable=True
    )

    skills = Column(
        Text,
        nullable=True
    )

    interests = Column(
        Text,
        nullable=True
    )

    # -----------------------------
    # Social Links
    # -----------------------------

    linkedin = Column(
        String(255),
        nullable=True
    )

    github = Column(
        String(255),
        nullable=True
    )

    portfolio = Column(
        String(255),
        nullable=True
    )

    # -----------------------------
    # Profile Image
    # -----------------------------

    profile_image = Column(
        String(255),
        nullable=True
    )

    # -----------------------------
    # Timestamps
    # -----------------------------

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # -----------------------------
    # Relationship
    # -----------------------------

    user = relationship(
        "User",
        back_populates="profile"
    )