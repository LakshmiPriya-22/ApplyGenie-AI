from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user

from app.models.resume import Resume
from app.services.resume_analysis_service import ResumeAnalysisService

router = APIRouter(
    prefix="/analyzer",
    tags=["AI Resume Analysis"]
)


@router.get("/latest")
def analyze_latest_resume(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Get the latest AI resume analysis.

    If no analysis exists, generate one automatically.
    """

    # ---------------------------------------
    # Get Latest Resume
    # ---------------------------------------
    resume = (
        db.query(Resume)
        .filter(
            Resume.user_id == current_user.id
        )
        .order_by(
            Resume.id.desc()
        )
        .first()
    )

    if resume is None:
        return {
            "message": "No resume uploaded."
        }

    # ---------------------------------------
    # Get Existing Analysis
    # ---------------------------------------
    analysis = ResumeAnalysisService.get_analysis(
        db=db,
        resume_id=resume.id
    )

    # ---------------------------------------
    # Generate Analysis If Missing
    # ---------------------------------------
    if analysis is None:

        analysis = ResumeAnalysisService.generate_analysis(
            db=db,
            resume=resume
        )

    # ---------------------------------------
    # Return JSON Analysis
    # ---------------------------------------
    return analysis.analysis


@router.post("/regenerate")
def regenerate_latest_resume_analysis(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Force regenerate the latest resume analysis.
    Useful during development.
    """

    resume = (
        db.query(Resume)
        .filter(
            Resume.user_id == current_user.id
        )
        .order_by(
            Resume.id.desc()
        )
        .first()
    )

    if resume is None:
        return {
            "message": "No resume uploaded."
        }

    analysis = ResumeAnalysisService.regenerate_analysis(
        db=db,
        resume=resume
    )

    return analysis.analysis