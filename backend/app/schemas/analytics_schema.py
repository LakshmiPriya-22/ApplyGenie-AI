from typing import List

from pydantic import BaseModel


class AnalyticsResponse(BaseModel):
    average_match_score: float

    applications_this_week: int

    applications_this_month: int

    most_applied_company: str | None

    most_applied_role: str | None

    top_locations: List[str]