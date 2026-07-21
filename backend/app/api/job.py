from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user

from app.schemas.job_schema import (
    JobCreate,
    JobUpdate,
    JobResponse,
    DeleteJobResponse
)

from app.services.job_service import JobService

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


# -------------------------------
# Create Job
# -------------------------------
@router.post(
    "",
    response_model=JobResponse,
    status_code=201
)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return JobService.create_job(
        db=db,
        job=job,
        current_user=current_user
    )


# -------------------------------
# Get All Jobs
# -------------------------------
@router.get(
    "",
    response_model=list[JobResponse]
)
def get_all_jobs(
    db: Session = Depends(get_db)
):
    return JobService.get_all_jobs(db=db)


# -------------------------------
# Get My Jobs
# -------------------------------
@router.get(
    "/my",
    response_model=list[JobResponse]
)
def get_my_jobs(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return JobService.get_my_jobs(
        db=db,
        current_user=current_user
    )


# -------------------------------
# Get Job By ID
# -------------------------------
@router.get(
    "/{job_id}",
    response_model=JobResponse
)
def get_job(
    job_id: int,
    db: Session = Depends(get_db)
):
    return JobService.get_job(
        db=db,
        job_id=job_id
    )


# -------------------------------
# Update Job
# -------------------------------
@router.put(
    "/{job_id}",
    response_model=JobResponse
)
def update_job(
    job_id: int,
    job_update: JobUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return JobService.update_job(
        db=db,
        job_id=job_id,
        job_update=job_update,
        current_user=current_user
    )


# -------------------------------
# Delete Job
# -------------------------------
@router.delete(
    "/{job_id}",
    response_model=DeleteJobResponse
)
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return JobService.delete_job(
        db=db,
        job_id=job_id,
        current_user=current_user
    )