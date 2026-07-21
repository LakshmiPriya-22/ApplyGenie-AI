from datetime import datetime
from typing import Any

from pydantic import BaseModel


class JobMatchResponse(BaseModel):
    id: int
    resume_id: int
    job_id: int
    match_score: float

    strengths: list[str]
    missing_skills: list[str]
    recommendations: list[str]

    summary: str

    ai_response: dict[str, Any]

    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class JobMatchResult(BaseModel):
    match_score: float

    strengths: list[str]

    missing_skills: list[str]

    recommendations: list[str]

    summary: str