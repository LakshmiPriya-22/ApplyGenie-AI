from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.logger import logger

from app.repositories.interview_repository import InterviewRepository
from app.repositories.resume_repository import ResumeRepository
from app.repositories.resume_analysis_repository import ResumeAnalysisRepository
from app.repositories.job_repository import JobRepository
from app.repositories.job_match_repository import JobMatchRepository

from app.services.ai_matching_service import AIMatchingService
from app.services.ai_interview_service import AIInterviewService


class InterviewService:

    @staticmethod
    def generate_interview(
        db: Session,
        resume_id: int,
        job_id: int,
        interview_type: str,
        difficulty: str,
        current_user
    ):

        logger.info(
            f"Generating interview for Resume {resume_id} and Job {job_id}"
        )

        # -----------------------------
        # Verify Resume
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

        if resume.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        # -----------------------------
        # Verify Job
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
        # Resume Analysis
        # -----------------------------
        analysis = ResumeAnalysisRepository.get_by_resume_id(
            db=db,
            resume_id=resume_id
        )

        if not analysis:
            raise HTTPException(
                status_code=404,
                detail="Resume analysis not found."
            )

        # -----------------------------
        # Get Existing Job Match
        # -----------------------------
        match = JobMatchRepository.get_match(
            db=db,
            resume_id=resume_id,
            job_id=job_id
        )

        # -----------------------------
        # Generate Match if Missing
        # -----------------------------
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

        # -----------------------------
        # Check Existing Interview
        # -----------------------------
        interview = InterviewRepository.interview_exists(
            db=db,
            resume_id=resume_id,
            job_id=job_id,
            interview_type=interview_type,
            difficulty=difficulty
        )

        if interview:
            return interview

        # -----------------------------
        # Generate Questions
        # -----------------------------
        questions = AIInterviewService.generate_interview(
            resume_analysis=analysis.analysis,
            job=job,
            match=match,
            interview_type=interview_type,
            difficulty=difficulty
        )

        # -----------------------------
        # Save Interview
        # -----------------------------
        interview = InterviewRepository.create_interview(
            db=db,
            user_id=current_user.id,
            resume_id=resume_id,
            job_id=job_id,
            job_match_id=match.id,
            interview_type=interview_type,
            difficulty=difficulty,
            questions=questions
        )

        logger.info(
            f"Interview {interview.id} created successfully."
        )

        return interview

    @staticmethod
    def submit_answers(
        db: Session,
        interview_id: int,
        answers: list,
        current_user
    ):

        interview = InterviewRepository.get_interview_by_id(
            db=db,
            interview_id=interview_id
        )

        if not interview:
            raise HTTPException(
                status_code=404,
                detail="Interview not found."
            )

        if interview.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        InterviewRepository.update_answers(
            db=db,
            interview=interview,
            answers=answers
        )

        result = AIInterviewService.evaluate_answers(
            questions=interview.questions,
            answers=answers
        )

        InterviewRepository.update_feedback(
            db=db,
            interview=interview,
            feedback=result,
            score=result["score"]
        )

        return interview

    @staticmethod
    def get_interview(
        db: Session,
        interview_id: int,
        current_user
    ):

        interview = InterviewRepository.get_interview_by_id(
            db=db,
            interview_id=interview_id
        )

        if not interview:
            raise HTTPException(
                status_code=404,
                detail="Interview not found."
            )

        if interview.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        return interview

    @staticmethod
    def get_my_interviews(
        db: Session,
        current_user
    ):

        return InterviewRepository.get_user_interviews(
            db=db,
            user_id=current_user.id
        )

    @staticmethod
    def delete_interview(
        db: Session,
        interview_id: int,
        current_user
    ):

        interview = InterviewRepository.get_interview_by_id(
            db=db,
            interview_id=interview_id
        )

        if not interview:
            raise HTTPException(
                status_code=404,
                detail="Interview not found."
            )

        if interview.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        InterviewRepository.delete_interview(
            db=db,
            interview=interview
        )

        return {
            "message": "Interview deleted successfully."
        }