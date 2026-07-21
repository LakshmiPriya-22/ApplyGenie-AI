from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ApplicationCreate(BaseModel):
    resume_id: int
    job_id: int


class ApplicationStatusUpdate(BaseModel):
    status: str
    recruiter_notes: Optional[str] = None


class ApplicationResponse(BaseModel):
    id: int
    user_id: int
    resume_id: int
    job_id: int

    status: str
    recruiter_notes: Optional[str] = None

    applied_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ApplicationDetailsResponse(BaseModel):
    id: int

    job_id: int
    title: str
    company: str
    location: str

    resume_id: int

    status: str
    recruiter_notes: Optional[str] = None

    applied_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class DeleteApplicationResponse(BaseModel):
    message: str