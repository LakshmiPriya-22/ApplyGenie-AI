from datetime import datetime
from pydantic import BaseModel


# -----------------------------------------
# Create Notification
# -----------------------------------------
class NotificationCreate(BaseModel):
    title: str
    message: str
    type: str = "INFO"


# -----------------------------------------
# Notification Response
# -----------------------------------------
class NotificationResponse(BaseModel):
    id: int
    title: str
    message: str
    type: str
    is_read: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }


# -----------------------------------------
# Mark Notification as Read
# -----------------------------------------
class NotificationReadResponse(BaseModel):
    message: str


# -----------------------------------------
# Delete Notification
# -----------------------------------------
class NotificationDeleteResponse(BaseModel):
    message: str