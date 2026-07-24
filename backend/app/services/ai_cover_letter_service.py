from app.core.logger import logger
from app.rag.rag_service import RAGService


class AICoverLetterService:

    @staticmethod
    def generate_cover_letter(
        resume,
        job,
        match
    ):
        """
        Generate a personalized cover letter using RAG.
        """

        logger.info(
            "Generating AI cover letter..."
        )

        company = job.company
        role = job.title

        cover_letter = RAGService.cover_letter(
            user_id=resume.user_id,
            resume_id=resume.id,
            company=company,
            role=role
        )

        logger.info(
            "Cover letter generated successfully."
        )

        return cover_letter