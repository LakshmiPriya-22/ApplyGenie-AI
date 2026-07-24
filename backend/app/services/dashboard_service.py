from sqlalchemy.orm import Session

from app.repositories.dashboard_repository import DashboardRepository


class DashboardService:

    @staticmethod
    def get_dashboard(
        db: Session,
        current_user
    ):

        return DashboardRepository.get_dashboard_data(
            db=db,
            user_id=current_user.id
        )