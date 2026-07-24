from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.schemas.resume_optimizer import ResumeOptimizerRequest
from app.services.resume_optimizer_service import ResumeOptimizerService

router = APIRouter(
    prefix="/resume-optimizer",
    tags=["Resume Optimizer"]
)


@router.post("/")
def optimize_resume(
    request: ResumeOptimizerRequest,
    current_user=Depends(get_current_user)
):
    return ResumeOptimizerService.optimize_resume(
        user_id=current_user.id,
        resume_id=request.resume_id,
        job_description=request.job_description
    )