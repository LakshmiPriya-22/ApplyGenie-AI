from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.logger import logger

from app.repositories.cover_letter_repository import CoverLetterRepository
from app.repositories.resume_repository import ResumeRepository
from app.repositories.resume_analysis_repository import ResumeAnalysisRepository
from app.repositories.job_repository import JobRepository
from app.repositories.job_match_repository import JobMatchRepository

from app.services.ai_matching_service import AIMatchingService
from app.services.ai_cover_letter_service import AICoverLetterService


class CoverLetterService:

    @staticmethod
    def generate_cover_letter(
        db: Session,
        resume_id: int,
        job_id: int,
        current_user
    ):

        logger.info(
            f"Generating cover letter for Resume {resume_id} and Job {job_id}"
        )

        # --------------------------------
        # Verify Resume
        # --------------------------------
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

        # --------------------------------
        # Verify Job
        # --------------------------------
        job = JobRepository.get_job_by_id(
            db=db,
            job_id=job_id
        )

        if not job:
            raise HTTPException(
                status_code=404,
                detail="Job not found."
            )

        # --------------------------------
        # Get Resume Analysis
        # --------------------------------
        analysis = ResumeAnalysisRepository.get_by_resume_id(
            db=db,
            resume_id=resume_id
        )

        if not analysis:
            raise HTTPException(
                status_code=404,
                detail="Resume analysis not found."
            )

        # --------------------------------
        # Get Existing Job Match
        # --------------------------------
        match = JobMatchRepository.get_match(
            db=db,
            resume_id=resume_id,
            job_id=job_id
        )

        # --------------------------------
        # Generate Match if Missing
        # --------------------------------
        if not match:

            logger.info("Generating new job match...")

            ai_result = AIMatchingService.match_resume_with_job(
                resume_analysis=analysis.analysis,
                job=job
            )

            match = JobMatchRepository.create_match(
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

        # --------------------------------
        # Generate Cover Letter
        # --------------------------------
        content = AICoverLetterService.generate_cover_letter(
            resume_analysis=analysis.analysis,
            job=job,
            match=match
        )

        # --------------------------------
        # Save or Update Cover Letter
        # --------------------------------
        existing = CoverLetterRepository.cover_letter_exists(
            db=db,
            resume_id=resume_id,
            job_id=job_id
        )

        if existing:

            logger.info("Updating existing cover letter...")

            return CoverLetterRepository.update_cover_letter(
                db=db,
                cover_letter=existing,
                content=content
            )

        logger.info("Creating new cover letter...")

        return CoverLetterRepository.create_cover_letter(
            db=db,
            user_id=current_user.id,
            resume_id=resume_id,
            job_id=job_id,
            job_match_id=match.id,
            content=content
        )

    @staticmethod
    def get_cover_letter(
        db: Session,
        cover_letter_id: int,
        current_user
    ):

        cover_letter = CoverLetterRepository.get_cover_letter_by_id(
            db=db,
            cover_letter_id=cover_letter_id
        )

        if not cover_letter:
            raise HTTPException(
                status_code=404,
                detail="Cover letter not found."
            )

        if cover_letter.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        return cover_letter

    @staticmethod
    def get_my_cover_letters(
        db: Session,
        current_user
    ):

        return CoverLetterRepository.get_user_cover_letters(
            db=db,
            user_id=current_user.id
        )

    @staticmethod
    def delete_cover_letter(
        db: Session,
        cover_letter_id: int,
        current_user
    ):

        cover_letter = CoverLetterRepository.get_cover_letter_by_id(
            db=db,
            cover_letter_id=cover_letter_id
        )

        if not cover_letter:
            raise HTTPException(
                status_code=404,
                detail="Cover letter not found."
            )

        if cover_letter.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        CoverLetterRepository.delete_cover_letter(
            db=db,
            cover_letter=cover_letter
        )

        return {
            "message": "Cover letter deleted successfully."
        }