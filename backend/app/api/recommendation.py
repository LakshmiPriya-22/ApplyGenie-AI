from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.schemas.recommendation_schema import RecommendationListResponse
from app.services.recommendation_service import RecommendationService

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


# -----------------------------------------
# Get Job Recommendations
# -----------------------------------------
@router.get(
    "/resume/{resume_id}",
    response_model=RecommendationListResponse
)
def get_recommendations(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return RecommendationService.get_recommendations(
        db=db,
        resume_id=resume_id,
        current_user=current_user
    )


# -----------------------------------------
# Refresh Recommendations
# -----------------------------------------
@router.post(
    "/resume/{resume_id}/refresh",
    response_model=RecommendationListResponse
)
def refresh_recommendations(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return RecommendationService.refresh_recommendations(
        db=db,
        resume_id=resume_id,
        current_user=current_user
    )