from app.rag.rag_service import RAGService


class ResumeOptimizerService:

    @staticmethod
    def optimize_resume(
        user_id: int,
        resume_id: int,
        job_description: str
    ):

        return RAGService.resume_optimizer(
            user_id=user_id,
            resume_id=resume_id,
            job_description=job_description
        )