from datetime import datetime, date, timedelta

from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.interview_schedule import InterviewSchedule


class InterviewScheduleRepository:

    @staticmethod
    def create_schedule(db: Session, schedule: InterviewSchedule):
        db.add(schedule)
        db.commit()
        db.refresh(schedule)
        return schedule

    @staticmethod
    def get_by_id(db: Session, schedule_id: int):
        return (
            db.query(InterviewSchedule)
            .filter(InterviewSchedule.id == schedule_id)
            .first()
        )

    @staticmethod
    def get_user_schedules(db: Session, user_id: int):
        return (
            db.query(InterviewSchedule)
            .filter(InterviewSchedule.user_id == user_id)
            .order_by(InterviewSchedule.scheduled_at)
            .all()
        )

    @staticmethod
    def get_upcoming(db: Session, user_id: int):
        return (
            db.query(InterviewSchedule)
            .filter(
                InterviewSchedule.user_id == user_id,
                InterviewSchedule.scheduled_at >= datetime.now(),
                InterviewSchedule.status == "Scheduled"
            )
            .order_by(InterviewSchedule.scheduled_at)
            .all()
        )

    @staticmethod
    def get_today(db: Session, user_id: int):
        today = date.today()

        return (
            db.query(InterviewSchedule)
            .filter(
                InterviewSchedule.user_id == user_id,
                func.date(InterviewSchedule.scheduled_at) == today
            )
            .order_by(InterviewSchedule.scheduled_at)
            .all()
        )

    @staticmethod
    def get_this_week(db: Session, user_id: int):
        today = date.today()

        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)

        return (
            db.query(InterviewSchedule)
            .filter(
                InterviewSchedule.user_id == user_id,
                func.date(InterviewSchedule.scheduled_at) >= start,
                func.date(InterviewSchedule.scheduled_at) <= end
            )
            .order_by(InterviewSchedule.scheduled_at)
            .all()
        )

    @staticmethod
    def update_schedule(
        db: Session,
        schedule: InterviewSchedule,
        scheduled_at: datetime
    ):
        schedule.scheduled_at = scheduled_at
        db.commit()
        db.refresh(schedule)
        return schedule

    @staticmethod
    def cancel_schedule(
        db: Session,
        schedule: InterviewSchedule
    ):
        schedule.status = "Cancelled"
        db.commit()
        db.refresh(schedule)
        return schedule

    @staticmethod
    def statistics(db: Session, user_id: int):

        total = (
            db.query(InterviewSchedule)
            .filter(InterviewSchedule.user_id == user_id)
            .count()
        )

        scheduled = (
            db.query(InterviewSchedule)
            .filter(
                InterviewSchedule.user_id == user_id,
                InterviewSchedule.status == "Scheduled"
            )
            .count()
        )

        completed = (
            db.query(InterviewSchedule)
            .filter(
                InterviewSchedule.user_id == user_id,
                InterviewSchedule.status == "Completed"
            )
            .count()
        )

        cancelled = (
            db.query(InterviewSchedule)
            .filter(
                InterviewSchedule.user_id == user_id,
                InterviewSchedule.status == "Cancelled"
            )
            .count()
        )

        upcoming = (
            db.query(InterviewSchedule)
            .filter(
                InterviewSchedule.user_id == user_id,
                InterviewSchedule.status == "Scheduled",
                InterviewSchedule.scheduled_at >= datetime.now()
            )
            .count()
        )

        return {
            "total": total,
            "scheduled": scheduled,
            "completed": completed,
            "cancelled": cancelled,
            "upcoming": upcoming
        }