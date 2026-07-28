from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


# ---------------------------------------
# Schedule Interview
# ---------------------------------------

class InterviewScheduleCreate(BaseModel):
    application_id: int
    company: str
    job_title: str
    interviewer_name: Optional[str] = None
    mode: str
    meeting_link: Optional[str] = None
    location: Optional[str] = None
    scheduled_at: datetime
    recruiter_notes: Optional[str] = None


# ---------------------------------------
# Update Schedule
# ---------------------------------------

class InterviewScheduleUpdate(BaseModel):
    scheduled_at: datetime


# ---------------------------------------
# Cancel Interview
# ---------------------------------------

class InterviewScheduleCancel(BaseModel):
    status: str = "Cancelled"


# ---------------------------------------
# Response
# ---------------------------------------

class InterviewScheduleResponse(BaseModel):
    id: int
    user_id: int
    application_id: int

    company: str
    job_title: str

    interviewer_name: Optional[str] = None

    mode: str
    meeting_link: Optional[str] = None
    location: Optional[str] = None

    scheduled_at: datetime

    status: str

    notes: Optional[str] = None

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ---------------------------------------
# Statistics
# ---------------------------------------

class InterviewStatistics(BaseModel):
    total: int
    scheduled: int
    completed: int
    cancelled: int
    upcoming: int