from datetime import datetime

from pydantic import BaseModel, ConfigDict


# ---------------------------------------
# Generate Cover Letter
# ---------------------------------------

class CoverLetterCreate(BaseModel):
    resume_id: int
    job_id: int


# ---------------------------------------
# Cover Letter Response
# ---------------------------------------

class CoverLetterResponse(BaseModel):
    id: int

    user_id: int
    resume_id: int
    job_id: int
    job_match_id: int

    content: str

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ---------------------------------------
# Delete Response
# ---------------------------------------

class DeleteCoverLetterResponse(BaseModel):
    message: str