from datetime import datetime

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.schemas.application_schema import (
    ApplicationCreate,
    ApplicationResponse,
    ApplicationStatusUpdate,
    DeleteApplicationResponse,
    ApplicationDashboardResponse
)

from app.services.application_service import ApplicationService

router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)


# ----------------------------------
# Apply for Job
# ----------------------------------
@router.post(
    "",
    response_model=ApplicationResponse
)
def apply_job(
    application: ApplicationCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ApplicationService.apply_job(
        db=db,
        resume_id=application.resume_id,
        job_id=application.job_id,
        current_user=current_user
    )


# ----------------------------------
# Get My Applications
# ----------------------------------
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


# ----------------------------------
# Get Application By ID
# ----------------------------------
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


# ----------------------------------
# Update Status
# ----------------------------------
@router.put(
    "/{application_id}",
    response_model=ApplicationResponse
)
def update_status(
    application_id: int,
    update: ApplicationStatusUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ApplicationService.update_status(
        db=db,
        application_id=application_id,
        status=update.status,
        notes=update.notes,
        current_user=current_user
    )


# ----------------------------------
# Withdraw Application
# ----------------------------------
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


# ----------------------------------
# Search Applications
# ----------------------------------
@router.get(
    "/search/"
)
def search_applications(
    company: str | None = Query(None),
    title: str | None = Query(None),
    status: str | None = Query(None),
    location: str | None = Query(None),
    from_date: datetime | None = Query(None),
    to_date: datetime | None = Query(None),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ApplicationService.search_applications(
        db=db,
        current_user=current_user,
        company=company,
        title=title,
        status=status,
        location=location,
        from_date=from_date,
        to_date=to_date
    )


# ----------------------------------
# Dashboard
# ----------------------------------
@router.get(
    "/dashboard",
    response_model=ApplicationDashboardResponse
)
def dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ApplicationService.get_dashboard(
        db=db,
        current_user=current_user
    )