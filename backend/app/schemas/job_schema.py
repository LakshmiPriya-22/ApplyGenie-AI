from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# ---------------------------------------
# Create Job
# ---------------------------------------
class JobCreate(BaseModel):
    title: str
    company: str
    location: str
    employment_type: str
    experience_level: str
    salary: Optional[str] = None
    description: str
    requirements: str
    skills: Optional[str] = None


# ---------------------------------------
# Update Job
# ---------------------------------------
class JobUpdate(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    employment_type: Optional[str] = None
    experience_level: Optional[str] = None
    salary: Optional[str] = None
    description: Optional[str] = None
    requirements: Optional[str] = None
    skills: Optional[str] = None


# ---------------------------------------
# Job Response
# ---------------------------------------
class JobResponse(BaseModel):
    id: int

    title: str
    company: str
    location: str
    employment_type: str
    experience_level: str

    salary: Optional[str] = None

    description: str
    requirements: str
    skills: Optional[str] = None

    # External jobs may not have a creator
    posted_by: Optional[int] = None

    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


# ---------------------------------------
# Delete Response
# ---------------------------------------
class DeleteJobResponse(BaseModel):
    message: str