from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class InterviewScheduleCreate(BaseModel):
    application_id: int
    company: str
    job_title: str
    interviewer_name: Optional[str] = None
    mode: str
    meeting_link: Optional[str] = None
    location: Optional[str] = None
    scheduled_at: datetime
    notes: Optional[str] = None


class InterviewScheduleUpdate(BaseModel):
    scheduled_at: datetime


class InterviewScheduleCancel(BaseModel):
    status: str = "Cancelled"


class InterviewScheduleResponse(BaseModel):
    id: int
    user_id: int
    application_id: int
    company: str
    job_title: str
    interviewer_name: Optional[str]
    mode: str
    meeting_link: Optional[str]
    location: Optional[str]
    scheduled_at: datetime
    status: str
    notes: Optional[str]
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class InterviewStatistics(BaseModel):
    total: int
    scheduled: int
    completed: int
    cancelled: int
    upcoming: int