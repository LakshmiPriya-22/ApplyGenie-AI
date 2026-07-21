from pydantic import BaseModel, ConfigDict
from typing import List


class RecommendationResponse(BaseModel):
    job_id: int
    title: str
    company: str
    location: str
    employment_type: str
    experience_level: str
    salary: str | None = None
    match_score: float
    summary: str

    model_config = ConfigDict(from_attributes=True)


class RecommendationListResponse(BaseModel):
    recommendations: List[RecommendationResponse]