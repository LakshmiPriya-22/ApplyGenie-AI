from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


# --------------------------------------
# Generate Interview Request
# --------------------------------------
class InterviewGenerateRequest(BaseModel):
    resume_id: int
    job_id: int
    job_match_id: int


# --------------------------------------
# Individual Question
# --------------------------------------
class InterviewQuestion(BaseModel):
    question: str
    difficulty: str


# --------------------------------------
# Interview Response
# --------------------------------------
class InterviewResponse(BaseModel):
    id: int

    user_id: int
    resume_id: int
    job_id: int
    job_match_id: int

    interview_type: str
    difficulty: str

    questions: list
    answers: Optional[list] = None
    feedback: Optional[list] = None

    tips: Optional[list] = None
    roadmap: Optional[list] = None

    summary: Optional[str] = None

    score: Optional[float] = None

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# --------------------------------------
# Interview List
# --------------------------------------
class InterviewListResponse(BaseModel):
    interviews: list[InterviewResponse]


# --------------------------------------
# Delete Response
# --------------------------------------
class DeleteInterviewResponse(BaseModel):
    message: str