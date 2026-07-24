from sqlalchemy.orm import Session

from app.repositories.analytics_repository import AnalyticsRepository


class AnalyticsService:

    @staticmethod
    def get_analytics(
        db: Session,
        current_user
    ):

        return AnalyticsRepository.get_analytics(
            db=db,
            user_id=current_user.id
        )