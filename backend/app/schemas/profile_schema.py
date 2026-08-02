from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


# ---------------------------------------
# Create Profile
# ---------------------------------------

class ProfileCreate(BaseModel):

    full_name: str = Field(..., max_length=100)

    phone: Optional[str] = None
    date_of_birth: Optional[str] = None
    gender: Optional[str] = None

    college: Optional[str] = None
    degree: Optional[str] = None
    branch: Optional[str] = None
    current_year: Optional[str] = None
    cgpa: Optional[float] = None

    headline: Optional[str] = None
    bio: Optional[str] = None
    skills: Optional[str] = None
    interests: Optional[str] = None

    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None


# ---------------------------------------
# Update Profile
# ---------------------------------------

class ProfileUpdate(BaseModel):

    full_name: Optional[str] = None

    phone: Optional[str] = None
    date_of_birth: Optional[str] = None
    gender: Optional[str] = None

    college: Optional[str] = None
    degree: Optional[str] = None
    branch: Optional[str] = None
    current_year: Optional[str] = None
    cgpa: Optional[float] = None

    headline: Optional[str] = None
    bio: Optional[str] = None
    skills: Optional[str] = None
    interests: Optional[str] = None

    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None

    profile_image: Optional[str] = None


# ---------------------------------------
# Profile Response
# ---------------------------------------

class ProfileResponse(BaseModel):

    id: int
    user_id: int

    full_name: str

    phone: Optional[str]
    date_of_birth: Optional[str]
    gender: Optional[str]

    college: Optional[str]
    degree: Optional[str]
    branch: Optional[str]
    current_year: Optional[str]
    cgpa: Optional[float]

    headline: Optional[str]
    bio: Optional[str]
    skills: Optional[str]
    interests: Optional[str]

    linkedin: Optional[str]
    github: Optional[str]
    portfolio: Optional[str]

    profile_image: Optional[str]

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )