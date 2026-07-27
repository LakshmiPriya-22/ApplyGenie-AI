from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.resume_repository import ResumeRepository
from app.rag.rag_service import RAGService


class ResumeChatService:

    @staticmethod
    def ask_question(
        db: Session,
        resume_id: int,
        question: str,
        current_user
    ):

        resume = ResumeRepository.get_by_id(
            db=db,
            resume_id=resume_id
        )

        if not resume:
            raise HTTPException(
                status_code=404,
                detail="Resume not found."
            )

        if resume.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        answer = RAGService.resume_chat(
            user_id=current_user.id,
            resume_id=resume.id,
            question=question
        )

        return {
            "answer": answer
        }