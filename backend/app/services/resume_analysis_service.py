from sqlalchemy.orm import Session

from app.repositories.resume_analysis_repository import (
    ResumeAnalysisRepository
)
from app.rag.rag_service import RAGService
from app.services.notification_service import NotificationService


class ResumeAnalysisService:

    @staticmethod
    def generate_analysis(
        db: Session,
        resume
    ):
        """
        Generate AI-powered resume analysis using RAG.
        """

        existing = ResumeAnalysisRepository.get_by_resume_id(
            db=db,
            resume_id=resume.id
        )

        if existing:
            return existing

        analysis = RAGService.resume_analysis(
            user_id=resume.user_id,
            resume_id=resume.id
        )

        result = ResumeAnalysisRepository.create(
            db=db,
            resume_id=resume.id,
            analysis=analysis
        )

        # Create notification
        NotificationService.create_notification(
            db=db,
            user_id=resume.user_id,
            title="Resume Analysis Completed",
            message="Your AI resume analysis is ready.",
            type="INFO"
        )

        return result

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

            NotificationService.create_notification(
                db=db,
                user_id=resume.user_id,
                title="Resume Analysis Updated",
                message="Your resume analysis has been regenerated.",
                type="INFO"
            )

            return existing

        result = ResumeAnalysisRepository.create(
            db=db,
            resume_id=resume.id,
            analysis=analysis
        )

        NotificationService.create_notification(
            db=db,
            user_id=resume.user_id,
            title="Resume Analysis Completed",
            message="Your AI resume analysis is ready.",
            type="INFO"
        )

        return result

    @staticmethod
    def get_analysis(
        db: Session,
        resume_id: int
    ):
        return ResumeAnalysisRepository.get_by_resume_id(
            db=db,
            resume_id=resume_id
        )