import json

from app.core.logger import logger
from app.rag.rag_service import RAGService


class AIMatchingService:

    @staticmethod
    def match_resume_with_job(
        resume,
        job
    ):
        """
        Match a user's resume against a job using RAG.
        """

        logger.info(
            "Generating AI Resume-Job Match..."
        )

        job_description = f"""
Title: {job.title}

Company: {job.company}

Location: {job.location}

Employment Type: {job.employment_type}

Experience: {job.experience_level}

Description:
{job.description}

Requirements:
{job.requirements}

Skills:
{job.skills}
"""

        response = RAGService.ats_analysis(
            user_id=resume.user_id,
            resume_id=resume.id,
            job_description=job_description
        )

        logger.info(
            "AI Resume-Job Match completed."
        )

        try:
            return json.loads(response)

        except Exception:

            return {
                "match_score": 0,
                "strengths": [],
                "missing_skills": [],
                "recommendations": [],
                "summary": response
            }