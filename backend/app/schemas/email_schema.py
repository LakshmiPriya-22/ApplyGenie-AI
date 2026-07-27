from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict


# ---------------------------------------
# Send Email Request
# ---------------------------------------

class EmailSendRequest(BaseModel):
    application_id: int
    recipient_email: EmailStr


# ---------------------------------------
# Email Response
# ---------------------------------------

class EmailResponse(BaseModel):
    message: str
    status: str


# ---------------------------------------
# Email Log Response
# ---------------------------------------

class EmailLogResponse(BaseModel):
    id: int

    user_id: int
    application_id: int

    recipient_email: EmailStr
    subject: str

    status: str

    error_message: Optional[str] = None

    sent_at: Optional[datetime] = None

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ---------------------------------------
# Delete Email Log Response
# ---------------------------------------

class DeleteEmailLogResponse(BaseModel):
    message: str