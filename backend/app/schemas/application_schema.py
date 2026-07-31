from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

class JobInfo(BaseModel):
    id: int
    title: str
    company: str
    location: Optional[str] = None
    employment_type: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class ApplicationCreate(BaseModel):
    resume_id: int
    job_id: int


class ApplicationStatusUpdate(BaseModel):
    status: str
    notes: Optional[str] = None


class ApplicationResponse(BaseModel):
    id: int
    user_id: int
    resume_id: int
    job_id: int

    status: str
    notes: Optional[str] = None

    applied_at: datetime
    updated_at: datetime

    job: JobInfo

    model_config = ConfigDict(from_attributes=True)


class ApplicationDetailsResponse(BaseModel):
    id: int

    job_id: int
    title: str
    company: str
    location: str

    resume_id: int

    status: str
    notes: Optional[str] = None

    applied_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ApplicationDashboardResponse(BaseModel):
    total: int
    applied: int
    screening: int
    interview: int
    assessment: int
    offer: int
    rejected: int
    withdrawn: int


class DeleteApplicationResponse(BaseModel):
    message: str