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
    resume = (
        db.query(Resume)
        .filter(Resume.user_id == current_user.id)
        .order_by(Resume.id.desc())
        .first()
    )

    if resume is None:
        return {
            "success": False,
            "message": "No resume uploaded."
        }

    analysis = ResumeAnalysisService.get_analysis(
        db=db,
        resume_id=resume.id
    )

    if analysis is None:
        return {
            "success": False,
            "message": "Analysis not found."
        }

    return {
        "success": True,
        "resume_id": resume.id,
        "filename": resume.filename,
        "analysis": analysis.analysis,
        "created_at": analysis.created_at
    }