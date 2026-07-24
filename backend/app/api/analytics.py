from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.schemas.analytics_schema import AnalyticsResponse
from app.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get(
    "",
    response_model=AnalyticsResponse
)
def get_analytics(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return AnalyticsService.get_analytics(
        db=db,
        current_user=current_user
    )