from datetime import datetime
from typing import Any

from pydantic import BaseModel


class ResumeAnalysisResponse(BaseModel):
    resume_id: int
    status: str
    analysis: dict[str, Any]
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }