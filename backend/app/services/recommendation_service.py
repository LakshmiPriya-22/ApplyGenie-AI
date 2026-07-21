from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.logger import logger

from app.repositories.resume_repository import ResumeRepository
from app.repositories.resume_analysis_repository import ResumeAnalysisRepository
from app.repositories.job_repository import JobRepository
from app.repositories.job_match_repository import JobMatchRepository

from app.services.ai_matching_service import AIMatchingService


class RecommendationService:

    @staticmethod
    def get_recommendations(
        db: Session,
        resume_id: int,
        current_user,
        limit: int = 10
    ):

        logger.info(
            f"Generating recommendations for Resume {resume_id}"
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

        # -----------------------------
        # Verify Ownership
        # -----------------------------
        if resume.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
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
        # Get All Jobs
        # -----------------------------
        jobs = JobRepository.get_all_jobs(db)

        recommendations = []

        # -----------------------------
        # Generate/Re-use Matches
        # -----------------------------
        for job in jobs:

            match = JobMatchRepository.get_match(
                db=db,
                resume_id=resume.id,
                job_id=job.id
            )

            if not match:

                logger.info(
                    f"Generating match for Job {job.id}"
                )

                ai_result = AIMatchingService.match_resume_with_job(
                    resume_analysis=analysis.analysis,
                    job=job
                )

                match = JobMatchRepository.create_match(
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

            recommendations.append(
                {
                    "job_id": job.id,
                    "title": job.title,
                    "company": job.company,
                    "location": job.location,
                    "employment_type": job.employment_type,
                    "experience_level": job.experience_level,
                    "salary": job.salary,
                    "match_score": match.match_score,
                    "summary": match.summary
                }
            )

        # -----------------------------
        # Sort by Match Score
        # -----------------------------
        recommendations.sort(
            key=lambda x: x["match_score"],
            reverse=True
        )

        logger.info(
            "Recommendations generated successfully."
        )

        return {
            "recommendations": recommendations[:limit]
        }

    @staticmethod
    def refresh_recommendations(
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

        JobMatchRepository.delete_resume_matches(
            db=db,
            resume_id=resume_id
        )

        return RecommendationService.get_recommendations(
            db=db,
            resume_id=resume_id,
            current_user=current_user
        )