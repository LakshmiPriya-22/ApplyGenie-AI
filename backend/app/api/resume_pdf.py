from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from app.dependencies.auth import get_current_user
from app.schemas.resume_pdf import ResumePDFRequest
from app.services.resume_pdf_service import ResumePDFService

router = APIRouter(
    prefix="/resume-pdf",
    tags=["Resume PDF Export"]
)


@router.post("/")
def generate_resume_pdf(
    request: ResumePDFRequest,
    current_user=Depends(get_current_user)
):
    """
    Generate an ATS-optimized resume PDF for the logged-in user.
    """

    pdf_path = ResumePDFService.generate_pdf(
        user_id=current_user.id,
        resume_id=request.resume_id,
        job_description=request.job_description
    )

    return FileResponse(
        path=pdf_path,
        filename="ATS_Optimized_Resume.pdf",
        media_type="application/pdf"
    )