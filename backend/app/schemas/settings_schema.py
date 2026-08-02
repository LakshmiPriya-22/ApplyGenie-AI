from datetime import datetime

from pydantic import BaseModel


# -----------------------------------------
# Settings Response
# -----------------------------------------

class SettingsResponse(BaseModel):

    id: int
    user_id: int

    email_notifications: bool
    job_notifications: bool
    interview_notifications: bool

    theme: str

    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


# -----------------------------------------
# Update Settings
# -----------------------------------------

class SettingsUpdate(BaseModel):

    email_notifications: bool
    job_notifications: bool
    interview_notifications: bool

    theme: str


# -----------------------------------------
# Change Password
# -----------------------------------------

class ChangePasswordRequest(BaseModel):

    current_password: str
    new_password: str


# -----------------------------------------
# Message Response
# -----------------------------------------

class MessageResponse(BaseModel):

    message: str