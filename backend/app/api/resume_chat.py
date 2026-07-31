from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user

from app.models.resume import Resume

from app.schemas.resume_chat_schema import (
    ResumeChatRequest,
    ResumeChatResponse,
)

from app.services.resume_chat_service import ResumeChatService

router = APIRouter(
    prefix="/resume-chat",
    tags=["Resume Chat"]
)


@router.post(
    "/",
    response_model=ResumeChatResponse,
)
def resume_chat(
    request: ResumeChatRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    # Get the latest uploaded resume for the current user
    resume = (
        db.query(Resume)
        .filter(Resume.user_id == current_user.id)
        .order_by(Resume.id.desc())
        .first()
    )

    if resume is None:
        return {
            "answer": "Please upload a resume first."
        }

    return ResumeChatService.ask_question(
        db=db,
        resume_id=resume.id,
        question=request.question,
        current_user=current_user,
    )