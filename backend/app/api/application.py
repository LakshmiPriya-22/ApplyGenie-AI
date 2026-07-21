from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.schemas.application_schema import (
    ApplicationCreate,
    ApplicationResponse,
    DeleteApplicationResponse,
    ApplicationStatusUpdate
)

from app.services.application_service import ApplicationService

router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)


# ---------------------------------------
# Apply for a Job
# ---------------------------------------
@router.post(
    "",
    response_model=ApplicationResponse
)
def apply_job(
    request: ApplicationCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ApplicationService.apply_job(
        db=db,
        resume_id=request.resume_id,
        job_id=request.job_id,
        current_user=current_user
    )


# ---------------------------------------
# Get My Applications
# ---------------------------------------
@router.get(
    "",
    response_model=list[ApplicationResponse]
)
def get_my_applications(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ApplicationService.get_my_applications(
        db=db,
        current_user=current_user
    )


# ---------------------------------------
# Get Application By ID
# ---------------------------------------
@router.get(
    "/{application_id}",
    response_model=ApplicationResponse
)
def get_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ApplicationService.get_application(
        db=db,
        application_id=application_id,
        current_user=current_user
    )


# ---------------------------------------
# Update Application Status
# ---------------------------------------
@router.put(
    "/{application_id}/status",
    response_model=ApplicationResponse
)
def update_application_status(
    application_id: int,
    request: ApplicationStatusUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ApplicationService.update_status(
        db=db,
        application_id=application_id,
        status=request.status,
        recruiter_notes=request.recruiter_notes,
        current_user=current_user
    )


# ---------------------------------------
# Withdraw Application
# ---------------------------------------
@router.delete(
    "/{application_id}",
    response_model=DeleteApplicationResponse
)
def withdraw_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ApplicationService.withdraw_application(
        db=db,
        application_id=application_id,
        current_user=current_user
    )