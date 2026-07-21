from datetime import datetime

from pydantic import BaseModel


class ResumeResponse(BaseModel):
    id: int
    filename: str
    filepath: str
    uploaded_at: datetime

    model_config = {
        "from_attributes": True
    }


class ResumeUploadResponse(BaseModel):
    message: str
    resume_id: int
    filename: str


class DeleteResponse(BaseModel):
    message: str