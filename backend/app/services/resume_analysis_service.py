from sqlalchemy.orm import Session

from app.repositories.resume_analysis_repository import (
    ResumeAnalysisRepository
)
from app.rag.rag_service import RAGService


class ResumeAnalysisService:

    @staticmethod
    def generate_analysis(
        db: Session,
        resume
    ):
        """
        Generate AI-powered resume analysis using RAG.
        """

        # Check if analysis already exists
        existing = ResumeAnalysisRepository.get_by_resume_id(
            db=db,
            resume_id=resume.id
        )

        if existing:
            return existing

        # Generate analysis using RAG
        analysis = RAGService.resume_analysis(
            user_id=resume.user_id,
            resume_id=resume.id
        )

        # Save analysis
        return ResumeAnalysisRepository.create(
            db=db,
            resume_id=resume.id,
            analysis=analysis
        )

    @staticmethod
    def regenerate_analysis(
        db: Session,
        resume
    ):
        """
        Regenerate AI analysis for an existing resume.
        """

        analysis = RAGService.resume_analysis(
            user_id=resume.user_id,
            resume_id=resume.id
        )

        existing = ResumeAnalysisRepository.get_by_resume_id(
            db=db,
            resume_id=resume.id
        )

        if existing:
            existing.analysis = analysis
            db.commit()
            db.refresh(existing)
            return existing

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