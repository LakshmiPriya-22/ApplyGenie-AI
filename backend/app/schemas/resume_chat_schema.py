from datetime import datetime
from pydantic import BaseModel, Field


class ResumeChatRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Question to ask about the uploaded resume."
    )


class ResumeChatResponse(BaseModel):
    answer: str


class ChatMessageResponse(BaseModel):
    role: str
    content: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }