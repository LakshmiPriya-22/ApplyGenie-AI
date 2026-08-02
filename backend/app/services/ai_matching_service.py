from app.core.logger import logger
from app.rag.rag_service import RAGService


class AIMatchingService:

    @staticmethod
    def match_resume_with_job(
        resume,
        job
    ):
        """
        Generate an AI job match between a resume and a job.
        """

        logger.info("Generating AI Resume-Job Match...")

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

        try:

            result = RAGService.job_match(
                user_id=resume.user_id,
                resume_id=resume.id,
                job_description=job_description
            )

            logger.info("AI Resume-Job Match completed.")

            return result

        except Exception as e:

            logger.error(f"Job Matching Failed: {e}")

            return {
                "match_score": 0,
                "strengths": [],
                "missing_skills": [],
                "recommendations": [],
                "summary": "Unable to generate job match."
            }