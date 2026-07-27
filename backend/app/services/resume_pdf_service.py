from app.rag.rag_service import RAGService
from app.utils.pdf_generator import PDFGenerator


class ResumePDFService:

    @staticmethod
    def generate_pdf(
        user_id: int,
        resume_id: int,
        job_description: str
    ):

        optimized_resume = RAGService.resume_optimizer(
            user_id=user_id,
            resume_id=resume_id,
            job_description=job_description
        )

        pdf_path = PDFGenerator.generate(
            optimized_resume
        )

        return pdf_path