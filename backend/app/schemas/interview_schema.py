from datetime import datetime
from typing import Optional, List, Dict, Any

from pydantic import BaseModel, ConfigDict


# ---------------------------------------
# Generate Interview
# ---------------------------------------

class InterviewCreate(BaseModel):
    resume_id: int
    job_id: int
    interview_type: str
    difficulty: str


# ---------------------------------------
# Interview Question
# ---------------------------------------

class InterviewQuestion(BaseModel):
    question: str
    category: str


# ---------------------------------------
# Interview Answer
# ---------------------------------------

class InterviewAnswer(BaseModel):
    question: str
    answer: str


# ---------------------------------------
# Submit Answers
# ---------------------------------------

class InterviewSubmit(BaseModel):
    answers: List[InterviewAnswer]


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

    feedback: Optional[Dict[str, Any]] = None

    score: Optional[float] = None

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ---------------------------------------
# Interview Feedback
# ---------------------------------------

class InterviewFeedbackResponse(BaseModel):
    score: float

    strengths: List[str]

    weaknesses: List[str]

    suggestions: List[str]

    overall_feedback: str


# ---------------------------------------
# Delete Interview
# ---------------------------------------

class DeleteInterviewResponse(BaseModel):
    message: str