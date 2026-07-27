from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.logger import logger

from app.repositories.resume_repository import ResumeRepository
from app.repositories.resume_analysis_repository import ResumeAnalysisRepository
from app.repositories.job_repository import JobRepository
from app.repositories.job_match_repository import JobMatchRepository


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
        # Ensure Resume Analysis Exists
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
        jobs = JobRepository.get_all(db)

        recommendations = []

        # -----------------------------
        # Read Existing Matches
        # -----------------------------
        for job in jobs:

            match = JobMatchRepository.get_match(
                db=db,
                resume_id=resume.id,
                job_id=job.id
            )

            if not match:
                continue

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
        # Sort Recommendations
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
            resume_id=resume.id
        )

        return {
            "message": "Recommendation cache cleared. Please regenerate job matches before requesting recommendations."
        }