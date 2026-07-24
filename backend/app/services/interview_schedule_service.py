from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.logger import logger

from app.models.interview_schedule import InterviewSchedule
from app.repositories.application_repository import ApplicationRepository
from app.repositories.interview_schedule_repository import (
    InterviewScheduleRepository,
)


class InterviewScheduleService:

    @staticmethod
    def create_schedule(db: Session, request, current_user):

        application = ApplicationRepository.get_application_by_id(
            db=db,
            application_id=request.application_id
        )

        if not application:
            raise HTTPException(
                status_code=404,
                detail="Application not found."
            )

        if application.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        schedule = InterviewSchedule(
            user_id=current_user.id,
            application_id=request.application_id,
            company=request.company,
            job_title=request.job_title,
            interviewer_name=request.interviewer_name,
            mode=request.mode,
            meeting_link=request.meeting_link,
            location=request.location,
            scheduled_at=request.scheduled_at,
            status="Scheduled",
            notes=request.notes,
        )

        logger.info(
            f"Creating interview schedule for user {current_user.id}"
        )

        return InterviewScheduleRepository.create_schedule(
            db=db,
            schedule=schedule
        )

    @staticmethod
    def get_all(db: Session, current_user):

        return InterviewScheduleRepository.get_user_schedules(
            db=db,
            user_id=current_user.id
        )

    @staticmethod
    def get_upcoming(db: Session, current_user):

        return InterviewScheduleRepository.get_upcoming(
            db=db,
            user_id=current_user.id
        )

    @staticmethod
    def get_today(db: Session, current_user):

        return InterviewScheduleRepository.get_today(
            db=db,
            user_id=current_user.id
        )

    @staticmethod
    def get_this_week(db: Session, current_user):

        return InterviewScheduleRepository.get_this_week(
            db=db,
            user_id=current_user.id
        )

    @staticmethod
    def reschedule(
        db: Session,
        schedule_id: int,
        scheduled_at,
        current_user
    ):

        schedule = InterviewScheduleRepository.get_by_id(
            db=db,
            schedule_id=schedule_id
        )

        if not schedule:
            raise HTTPException(
                status_code=404,
                detail="Interview schedule not found."
            )

        if schedule.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        logger.info(
            f"Rescheduling interview {schedule.id}"
        )

        return InterviewScheduleRepository.update_schedule(
            db=db,
            schedule=schedule,
            scheduled_at=scheduled_at
        )

    @staticmethod
    def cancel(
        db: Session,
        schedule_id: int,
        current_user
    ):

        schedule = InterviewScheduleRepository.get_by_id(
            db=db,
            schedule_id=schedule_id
        )

        if not schedule:
            raise HTTPException(
                status_code=404,
                detail="Interview schedule not found."
            )

        if schedule.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        logger.info(
            f"Cancelling interview {schedule.id}"
        )

        return InterviewScheduleRepository.cancel_schedule(
            db=db,
            schedule=schedule
        )

    @staticmethod
    def statistics(
        db: Session,
        current_user
    ):

        return InterviewScheduleRepository.statistics(
            db=db,
            user_id=current_user.id
        )