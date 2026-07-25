from app.rag.rag_service import RAGService


class JobMatchService:

    @staticmethod
    def match_resume(
        user_id: int,
        resume_id: int,
        job_description: str
    ):

        return RAGService.job_match(
            user_id=user_id,
            resume_id=resume_id,
            job_description=job_description
        )