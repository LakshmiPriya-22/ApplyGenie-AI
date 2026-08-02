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
from app.services.notification_service import NotificationService


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

        job = JobRepository.get_by_id(
            db=db,
            job_id=job_id
        )

        if not job:
            raise HTTPException(
                status_code=404,
                detail="Job not found."
            )

        analysis = ResumeAnalysisRepository.get_by_resume_id(
            db=db,
            resume_id=resume_id
        )

        if not analysis:
            raise HTTPException(
                status_code=404,
                detail="Resume analysis not found."
            )

        match = JobMatchRepository.get_match(
            db=db,
            resume_id=resume_id,
            job_id=job_id
        )

        if not match:

            logger.info("Generating new job match...")

            ai_result = AIMatchingService.match_resume_with_job(
                resume=resume,
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

        interview = InterviewRepository.interview_exists(
            db=db,
            resume_id=resume_id,
            job_id=job_id,
            interview_type=interview_type,
            difficulty=difficulty
        )

        if interview:
            return interview

        questions = AIInterviewService.generate_interview(
            resume=resume,
            job=job,
            match=match,
            interview_type=interview_type,
            difficulty=difficulty
        )

        interview = InterviewRepository.create_interview(
            db=db,
            user_id=current_user.id,
            resume_id=resume_id,
            job_id=job_id,
            job_match_id=match.id,
            interview_type=interview_type,
            difficulty=difficulty,
            questions=questions,
            tips=[],
            roadmap=[],
            summary=f"{interview_type} interview generated successfully."
        )

        NotificationService.create_notification(
            db=db,
            user_id=current_user.id,
            title="Interview Generated",
            message=f"Your {interview_type} interview for '{job.title}' is ready.",
            type="INTERVIEW"
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
            feedback={
                "strengths": result.get("strengths", []),
                "weaknesses": result.get("weaknesses", []),
                "suggestions": result.get("suggestions", []),
                "overall_feedback": result.get("overall_feedback", "")
            },
            score=result.get("score", 0)
        )

        NotificationService.create_notification(
            db=db,
            user_id=current_user.id,
            title="Interview Completed",
            message=f"You scored {result.get('score', 0)}% in your AI interview.",
            type="SUCCESS"
        )

        return InterviewRepository.get_interview_by_id(
            db=db,
            interview_id=interview_id
        )

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