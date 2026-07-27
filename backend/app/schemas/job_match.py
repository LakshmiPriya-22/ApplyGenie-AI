from fastapi import APIRouter, Depends

from app.schemas.job_match import JobMatchRequest
from app.services.job_match_service import JobMatchService
from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/job-match",
    tags=["Job Match"]
)


@router.post("/")
def job_match(
    request: JobMatchRequest,
    current_user=Depends(get_current_user)
):

    return JobMatchService.match_resume(
        user_id=current_user.id,
        resume_id=request.resume_id,
        job_description=request.job_description
    )