from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.schemas.interview_schedule_schema import (
    InterviewScheduleCreate,
    InterviewScheduleUpdate,
    InterviewScheduleResponse,
    InterviewStatistics,
)

from app.services.interview_schedule_service import (
    InterviewScheduleService,
)

router = APIRouter(
    prefix="/interview-schedules",
    tags=["Interview Scheduler"]
)


# --------------------------------------------------
# Schedule Interview
# --------------------------------------------------

@router.post(
    "",
    response_model=InterviewScheduleResponse
)
def create_interview_schedule(
    request: InterviewScheduleCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return InterviewScheduleService.create_schedule(
        db=db,
        request=request,
        current_user=current_user
    )


# --------------------------------------------------
# Get All Interviews
# --------------------------------------------------

@router.get(
    "",
    response_model=list[InterviewScheduleResponse]
)
def get_all_interviews(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return InterviewScheduleService.get_all(
        db=db,
        current_user=current_user
    )


# --------------------------------------------------
# Upcoming Interviews
# --------------------------------------------------

@router.get(
    "/upcoming",
    response_model=list[InterviewScheduleResponse]
)
def get_upcoming_interviews(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return InterviewScheduleService.get_upcoming(
        db=db,
        current_user=current_user
    )


# --------------------------------------------------
# Today's Interviews
# --------------------------------------------------

@router.get(
    "/today",
    response_model=list[InterviewScheduleResponse]
)
def get_today_interviews(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return InterviewScheduleService.get_today(
        db=db,
        current_user=current_user
    )


# --------------------------------------------------
# This Week's Interviews
# --------------------------------------------------

@router.get(
    "/week",
    response_model=list[InterviewScheduleResponse]
)
def get_week_interviews(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return InterviewScheduleService.get_this_week(
        db=db,
        current_user=current_user
    )


# --------------------------------------------------
# Reschedule Interview
# --------------------------------------------------

@router.patch(
    "/{schedule_id}/reschedule",
    response_model=InterviewScheduleResponse
)
def reschedule_interview(
    schedule_id: int,
    request: InterviewScheduleUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return InterviewScheduleService.reschedule(
        db=db,
        schedule_id=schedule_id,
        scheduled_at=request.scheduled_at,
        current_user=current_user
    )


# --------------------------------------------------
# Cancel Interview
# --------------------------------------------------

@router.patch(
    "/{schedule_id}/cancel",
    response_model=InterviewScheduleResponse
)
def cancel_interview(
    schedule_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return InterviewScheduleService.cancel(
        db=db,
        schedule_id=schedule_id,
        current_user=current_user
    )


# --------------------------------------------------
# Statistics
# --------------------------------------------------

@router.get(
    "/statistics",
    response_model=InterviewStatistics
)
def interview_statistics(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return InterviewScheduleService.statistics(
        db=db,
        current_user=current_user
    )