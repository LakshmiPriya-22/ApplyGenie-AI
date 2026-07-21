from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.schemas.interview_schema import (
    InterviewCreate,
    InterviewSubmit,
    InterviewResponse,
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
    request: InterviewCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return InterviewService.generate_interview(
        db=db,
        resume_id=request.resume_id,
        job_id=request.job_id,
        interview_type=request.interview_type,
        difficulty=request.difficulty,
        current_user=current_user
    )


# ---------------------------------------
# Submit Answers
# ---------------------------------------
@router.post(
    "/{interview_id}/submit",
    response_model=InterviewResponse
)
def submit_answers(
    interview_id: int,
    request: InterviewSubmit,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return InterviewService.submit_answers(
        db=db,
        interview_id=interview_id,
        answers=[answer.model_dump() for answer in request.answers],
        current_user=current_user
    )


# ---------------------------------------
# Get My Interviews
# ---------------------------------------
@router.get(
    "",
    response_model=list[InterviewResponse]
)
def get_my_interviews(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return InterviewService.get_my_interviews(
        db=db,
        current_user=current_user
    )


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