from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.application import Application


class DashboardRepository:

    @staticmethod
    def get_dashboard_data(
        db: Session,
        user_id: int
    ):

        statuses = [
            "Applied",
            "Shortlisted",
            "Interview Scheduled",
            "Interview Completed",
            "Offer Received",
            "Accepted",
            "Rejected",
            "Withdrawn"
        ]

        result = {}

        total = (
            db.query(func.count(Application.id))
            .filter(Application.user_id == user_id)
            .scalar()
        )

        result["total_applications"] = total

        for status in statuses:
            count = (
                db.query(func.count(Application.id))
                .filter(
                    Application.user_id == user_id,
                    Application.status == status
                )
                .scalar()
            )

            result[
                status.lower().replace(" ", "_")
            ] = count

        return result