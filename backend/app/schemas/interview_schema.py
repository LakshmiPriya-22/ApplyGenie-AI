from datetime import datetime
from typing import Optional, List, Dict, Any

from pydantic import BaseModel, ConfigDict


# ---------------------------------------
# Generate Interview Request
# ---------------------------------------

class InterviewGenerateRequest(BaseModel):
    resume_id: int
    job_id: int


# ---------------------------------------
# Interview Response
# ---------------------------------------

class InterviewResponse(BaseModel):
    id: int

    user_id: int
    resume_id: int
    job_id: int
    job_match_id: int

    interview_type: str
    difficulty: str

    questions: List[Dict[str, Any]]

    answers: Optional[List[Dict[str, Any]]] = None
    feedback: Optional[List[Dict[str, Any]]] = None

    tips: Optional[List[str]] = None
    roadmap: Optional[List[str]] = None

    summary: Optional[str] = None

    score: Optional[float] = None

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ---------------------------------------
# Interview List Response
# ---------------------------------------

class InterviewListResponse(BaseModel):
    interviews: List[InterviewResponse]


# ---------------------------------------
# Delete Response
# ---------------------------------------

class DeleteInterviewResponse(BaseModel):
    message: str