from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.schemas.interview_schema import (
    InterviewGenerateRequest,
    InterviewResponse,
    InterviewListResponse,
    DeleteInterviewResponse
)

from app.services.interview_service import InterviewService

router = APIRouter(
    prefix="/interviews",
    tags=["AI Interview Preparation"]
)


# ---------------------------------------
# Generate Interview
# ---------------------------------------
@router.post(
    "/generate",
    response_model=InterviewResponse
)
def generate_interview(
    request: InterviewGenerateRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return InterviewService.generate_interview(
        db=db,
        resume_id=request.resume_id,
        job_id=request.job_id,
        current_user=current_user,
        interview_type="Technical + HR",
        difficulty="Medium"
    )


# ---------------------------------------
# Get My Interviews
# ---------------------------------------
@router.get(
    "",
    response_model=InterviewListResponse
)
def get_my_interviews(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    interviews = InterviewService.get_my_interviews(
        db=db,
        current_user=current_user
    )

    return {
        "interviews": interviews
    }


# ---------------------------------------
# Get Interview By ID
# ---------------------------------------
@router.get(
    "/{interview_id}",
    response_model=InterviewResponse
)
def get_interview(
    interview_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return InterviewService.get_interview(
        db=db,
        interview_id=interview_id,
        current_user=current_user
    )


# ---------------------------------------
# Delete Interview
# ---------------------------------------
@router.delete(
    "/{interview_id}",
    response_model=DeleteInterviewResponse
)
def delete_interview(
    interview_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return InterviewService.delete_interview(
        db=db,
        interview_id=interview_id,
        current_user=current_user
    )