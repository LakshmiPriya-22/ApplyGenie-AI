from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.schemas.job_match_schema import (
    JobMatchResponse
)
from app.schemas.job_schema import DeleteJobResponse

from app.services.job_match_service import JobMatchService

router = APIRouter(
    prefix="/matches",
    tags=["Job Matching"]
)


# -----------------------------------
# Match Resume with Job
# -----------------------------------
@router.post(
    "/jobs/{job_id}/resume/{resume_id}",
    response_model=JobMatchResponse
)
def match_resume_with_job(
    job_id: int,
    resume_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return JobMatchService.match_resume_with_job(
        db=db,
        resume_id=resume_id,
        job_id=job_id,
        current_user=current_user
    )


# -----------------------------------
# Get Match By ID
# -----------------------------------
@router.get(
    "/{match_id}",
    response_model=JobMatchResponse
)
def get_match(
    match_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return JobMatchService.get_match(
        db=db,
        match_id=match_id,
        current_user=current_user
    )


# -----------------------------------
# Get All Matches For Resume
# -----------------------------------
@router.get(
    "/resume/{resume_id}",
    response_model=list[JobMatchResponse]
)
def get_resume_matches(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return JobMatchService.get_resume_matches(
        db=db,
        resume_id=resume_id,
        current_user=current_user
    )


# -----------------------------------
# Delete Match
# -----------------------------------
@router.delete(
    "/{match_id}",
    response_model=DeleteJobResponse
)
def delete_match(
    match_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return JobMatchService.delete_match(
        db=db,
        match_id=match_id,
        current_user=current_user
    )