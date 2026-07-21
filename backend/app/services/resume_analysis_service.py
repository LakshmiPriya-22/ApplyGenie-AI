from sqlalchemy.orm import Session

from app.repositories.resume_analysis_repository import (
    ResumeAnalysisRepository
)
from app.services.llm_service import LLMService


class ResumeAnalysisService:

    @staticmethod
    def generate_analysis(
        db: Session,
        resume
    ):
        # Check if analysis already exists
        existing = ResumeAnalysisRepository.get_by_resume_id(
            db=db,
            resume_id=resume.id
        )

        if existing:
            return existing

        # Generate new analysis
        analysis = LLMService.parse_resume(
            resume.extracted_text
        )

        return ResumeAnalysisRepository.create(
            db=db,
            resume_id=resume.id,
            analysis=analysis
        )

    @staticmethod
    def get_analysis(
        db: Session,
        resume_id: int
    ):
        return ResumeAnalysisRepository.get_by_resume_id(
            db=db,
            resume_id=resume_id
        )