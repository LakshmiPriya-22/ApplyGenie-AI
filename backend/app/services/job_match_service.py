from sqlalchemy.orm import Session

from app.rag.rag_service import RAGService

from app.repositories.job_repository import JobRepository
from app.repositories.job_match_repository import JobMatchRepository


class JobMatchService:

    @staticmethod
    def match_resume(
        db: Session,
        user_id: int,
        resume_id: int,
        job_id: int
    ):

        existing_match = JobMatchRepository.get_match(
            db=db,
            resume_id=resume_id,
            job_id=job_id
        )

        if existing_match:
            return existing_match

        job = JobRepository.get_by_id(
            db=db,
            job_id=job_id
        )

        if not job:
            raise Exception("Job not found.")

        ai_result = RAGService.job_match(
            user_id=user_id,
            resume_id=resume_id,
            job_description=job.description
        )

        job_match = JobMatchRepository.create_match(
            db=db,
            resume_id=resume_id,
            job_id=job_id,
            match_score=ai_result["match_score"],
            strengths=ai_result["strengths"],
            missing_skills=ai_result["missing_skills"],
            recommendations=ai_result["recommendations"],
            summary=ai_result["summary"],
            ai_response=ai_result
        )

        return job_match

    @staticmethod
    def get_match(
        db: Session,
        match_id: int
    ):
        return JobMatchRepository.get_match_by_id(
            db=db,
            match_id=match_id
        )

    @staticmethod
    def get_resume_matches(
        db: Session,
        resume_id: int
    ):
        return JobMatchRepository.get_matches_by_resume(
            db=db,
            resume_id=resume_id
        )

    @staticmethod
    def get_job_matches(
        db: Session,
        job_id: int
    ):
        return JobMatchRepository.get_matches_by_job(
            db=db,
            job_id=job_id
        )

    @staticmethod
    def delete_match(
        db: Session,
        match_id: int
    ):

        match = JobMatchRepository.get_match_by_id(
            db=db,
            match_id=match_id
        )

        if not match:
            raise Exception("Match not found.")

        JobMatchRepository.delete_match(
            db=db,
            job_match=match
        )

        return {
            "message": "Job match deleted successfully."
        }