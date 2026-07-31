from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


# ---------------------------------------
# Create Schedule
# ---------------------------------------

class InterviewScheduleCreate(BaseModel):
    interview_id: int
    scheduled_at: datetime


# ---------------------------------------
# Update Schedule
# ---------------------------------------

class InterviewScheduleUpdate(BaseModel):
    scheduled_at: datetime


# ---------------------------------------
# Schedule Response
# ---------------------------------------

class InterviewScheduleResponse(BaseModel):

    id: int

    user_id: int
    interview_id: int

    scheduled_at: datetime

    status: str

    reminder_sent: bool

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ---------------------------------------
# Statistics
# ---------------------------------------

class InterviewStatistics(BaseModel):

    total: int

    upcoming: int

    completed: int

    cancelled: int

    today: int

    this_week: int


# ---------------------------------------
# Delete Response
# ---------------------------------------

class DeleteInterviewScheduleResponse(BaseModel):
    message: str