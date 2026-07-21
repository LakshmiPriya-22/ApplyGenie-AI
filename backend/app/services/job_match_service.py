from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.logger import logger

from app.repositories.resume_repository import ResumeRepository
from app.repositories.job_repository import JobRepository
from app.repositories.resume_analysis_repository import ResumeAnalysisRepository
from app.repositories.job_match_repository import JobMatchRepository

from app.services.ai_matching_service import AIMatchingService


class JobMatchService:

    @staticmethod
    def match_resume_with_job(
        db: Session,
        resume_id: int,
        job_id: int,
        current_user
    ):

        logger.info(
            f"Matching Resume {resume_id} with Job {job_id}"
        )

        # -----------------------------
        # Verify Resume Exists
        # -----------------------------
        resume = ResumeRepository.get_by_id(
            db=db,
            resume_id=resume_id
        )

        if not resume:
            raise HTTPException(
                status_code=404,
                detail="Resume not found."
            )

        # -----------------------------
        # Verify Ownership
        # -----------------------------
        if resume.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        # -----------------------------
        # Verify Job Exists
        # -----------------------------
        job = JobRepository.get_job_by_id(
            db=db,
            job_id=job_id
        )

        if not job:
            raise HTTPException(
                status_code=404,
                detail="Job not found."
            )

        # -----------------------------
        # Get Resume Analysis
        # -----------------------------
        analysis = ResumeAnalysisRepository.get_by_resume_id(
            db=db,
            resume_id=resume.id
        )

        if not analysis:
            raise HTTPException(
                status_code=404,
                detail="Resume analysis not found."
            )

        # -----------------------------
        # Check Existing Match
        # -----------------------------
        existing_match = JobMatchRepository.get_match(
            db=db,
            resume_id=resume.id,
            job_id=job.id
        )

        if existing_match:

            logger.info(
                "Returning existing job match."
            )

            return existing_match

        # -----------------------------
        # AI Matching
        # -----------------------------
        ai_result = AIMatchingService.match_resume_with_job(
            resume_analysis=analysis.analysis,
            job=job
        )

        logger.info(
            "Saving AI matching result."
        )

        # -----------------------------
        # Save Match
        # -----------------------------
        job_match = JobMatchRepository.create_match(
            db=db,
            resume_id=resume.id,
            job_id=job.id,
            match_score=ai_result["match_score"],
            strengths=ai_result["strengths"],
            missing_skills=ai_result["missing_skills"],
            recommendations=ai_result["recommendations"],
            summary=ai_result["summary"],
            ai_response=ai_result
        )

        logger.info(
            f"Job Match {job_match.id} created successfully."
        )

        return job_match

    @staticmethod
    def get_match(
        db: Session,
        match_id: int,
        current_user
    ):

        match = JobMatchRepository.get_match_by_id(
            db=db,
            match_id=match_id
        )

        if not match:
            raise HTTPException(
                status_code=404,
                detail="Match not found."
            )

        if match.resume.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        return match

    @staticmethod
    def get_resume_matches(
        db: Session,
        resume_id: int,
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

        return JobMatchRepository.get_matches_by_resume(
            db=db,
            resume_id=resume_id
        )

    @staticmethod
    def delete_match(
        db: Session,
        match_id: int,
        current_user
    ):

        match = JobMatchRepository.get_match_by_id(
            db=db,
            match_id=match_id
        )

        if not match:
            raise HTTPException(
                status_code=404,
                detail="Match not found."
            )

        if match.resume.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        JobMatchRepository.delete_match(
            db=db,
            job_match=match
        )

        return {
            "message": "Match deleted successfully."
        }