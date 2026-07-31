from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.rag.rag_service import RAGService

from app.repositories.job_repository import JobRepository
from app.repositories.job_match_repository import JobMatchRepository
from app.services.notification_service import NotificationService

class JobMatchService:

    @staticmethod
    def match_resume(
        db: Session,
        user_id: int,
        resume_id: int,
        job_id: int,
    ):

        existing = JobMatchRepository.get_match(
            db=db,
            resume_id=resume_id,
            job_id=job_id,
        )

        if existing:
            return existing

        job = JobRepository.get_by_id(
            db=db,
            job_id=job_id,
        )

        if not job:
            raise HTTPException(
                status_code=404,
                detail="Job not found.",
            )

        ai_result = RAGService.job_match(
            user_id=user_id,
            resume_id=resume_id,
            job_description=job.description,
        )
        # Save match
        job_match= JobMatchRepository.create_match(
            db=db,
            resume_id=resume_id,
            job_id=job_id,
            match_score=ai_result["match_score"],
            strengths=ai_result["strengths"],
            missing_skills=ai_result["missing_skills"],
            recommendations=ai_result["recommendations"],
            summary=ai_result["summary"],
            ai_response=ai_result,
        )

        NotificationService.create_notification(
        db=db,
        user_id=user_id,
        title="Job Match Found",
        message=f"Your resume matched with '{job.title}' at {job.company}.",
        type="JOB",
    )
        return job_match 

    @staticmethod
    def get_match(
        db: Session,
        match_id: int,
    ):

        match = JobMatchRepository.get_match_by_id(
            db=db,
            match_id=match_id,
        )

        if not match:
            raise HTTPException(
                status_code=404,
                detail="Match not found.",
            )

        return match

    @staticmethod
    def get_resume_matches(
        db: Session,
        resume_id: int,
    ):

        return JobMatchRepository.get_matches_by_resume(
            db=db,
            resume_id=resume_id,
        )

    @staticmethod
    def get_job_matches(
        db: Session,
        job_id: int,
    ):

        return JobMatchRepository.get_matches_by_job(
            db=db,
            job_id=job_id,
        )

    @staticmethod
    def delete_match(
        db: Session,
        match_id: int,
    ):

        match = JobMatchRepository.get_match_by_id(
            db=db,
            match_id=match_id,
        )

        if not match:
            raise HTTPException(
                status_code=404,
                detail="Match not found.",
            )

        JobMatchRepository.delete_match(
            db=db,
            job_match=match,
        )

        return {
            "message": "Job match deleted successfully."
        }