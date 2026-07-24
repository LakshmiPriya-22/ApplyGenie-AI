from datetime import datetime, timedelta

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.application import Application
from app.models.job import Job
from app.models.job_match import JobMatch


class AnalyticsRepository:

    @staticmethod
    def get_analytics(
        db: Session,
        user_id: int
    ):

        today = datetime.utcnow()

        week_start = today - timedelta(days=7)

        month_start = today.replace(day=1)

        # ----------------------------------------
        # Average Match Score
        # ----------------------------------------

        average_match_score = (
            db.query(func.avg(JobMatch.match_score))
            .join(
                Application,
                JobMatch.resume_id == Application.resume_id
            )
            .filter(Application.user_id == user_id)
            .scalar()
        )

        if average_match_score is None:
            average_match_score = 0

        # ----------------------------------------
        # Applications This Week
        # ----------------------------------------

        applications_this_week = (
            db.query(func.count(Application.id))
            .filter(
                Application.user_id == user_id,
                Application.applied_at >= week_start
            )
            .scalar()
        )

        # ----------------------------------------
        # Applications This Month
        # ----------------------------------------

        applications_this_month = (
            db.query(func.count(Application.id))
            .filter(
                Application.user_id == user_id,
                Application.applied_at >= month_start
            )
            .scalar()
        )

        # ----------------------------------------
        # Most Applied Company
        # ----------------------------------------

        company = (
            db.query(
                Job.company,
                func.count(Application.id).label("count")
            )
            .join(
                Application,
                Job.id == Application.job_id
            )
            .filter(
                Application.user_id == user_id
            )
            .group_by(Job.company)
            .order_by(func.count(Application.id).desc())
            .first()
        )

        # ----------------------------------------
        # Most Applied Role
        # ----------------------------------------

        role = (
            db.query(
                Job.title,
                func.count(Application.id).label("count")
            )
            .join(
                Application,
                Job.id == Application.job_id
            )
            .filter(
                Application.user_id == user_id
            )
            .group_by(Job.title)
            .order_by(func.count(Application.id).desc())
            .first()
        )

        # ----------------------------------------
        # Top Locations
        # ----------------------------------------

        locations = (
            db.query(
                Job.location,
                func.count(Application.id).label("count")
            )
            .join(
                Application,
                Job.id == Application.job_id
            )
            .filter(
                Application.user_id == user_id
            )
            .group_by(Job.location)
            .order_by(func.count(Application.id).desc())
            .limit(3)
            .all()
        )

        return {
            "average_match_score": round(float(average_match_score), 2),
            "applications_this_week": applications_this_week,
            "applications_this_month": applications_this_month,
            "most_applied_company": company[0] if company else None,
            "most_applied_role": role[0] if role else None,
            "top_locations": [location[0] for location in locations]
        }