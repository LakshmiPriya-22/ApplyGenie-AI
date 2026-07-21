from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user

from app.schemas.resume_schema import (
    ResumeResponse,
    ResumeUploadResponse,
    DeleteResponse
)
from app.schemas.resume_analysis_schema import ResumeAnalysisResponse

from app.services.resume_service import ResumeService
from app.services.resume_analysis_service import ResumeAnalysisService

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


# -------------------------------
# Upload Resume
# -------------------------------
@router.post(
    "/upload",
    response_model=ResumeUploadResponse
)
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return ResumeService.upload_resume(
        db=db,
        file=file,
        current_user=current_user
    )


# -------------------------------
# Get All Resumes of Logged-in User
# -------------------------------
@router.get(
    "",
    response_model=list[ResumeResponse]
)
def get_all_resumes(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return ResumeService.get_all_resumes(
        db=db,
        current_user=current_user
    )


# -------------------------------
# Get Resume By ID
# -------------------------------
@router.get(
    "/{resume_id}",
    response_model=ResumeResponse
)
def get_resume(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return ResumeService.get_resume(
        db=db,
        resume_id=resume_id,
        current_user=current_user
    )


# -------------------------------
# Get Resume Analysis
# -------------------------------
@router.get(
    "/{resume_id}/analysis",
    response_model=ResumeAnalysisResponse
)
def get_resume_analysis(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    analysis = ResumeAnalysisService.get_analysis(
        db=db,
        resume_id=resume_id
    )

    if not analysis:
        raise HTTPException(
            status_code=404,
            detail="Resume analysis not found."
        )

    return analysis


# -------------------------------
# Delete Resume
# -------------------------------
@router.delete(
    "/{resume_id}",
    response_model=DeleteResponse
)
def delete_resume(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return ResumeService.delete_resume(
        db=db,
        resume_id=resume_id,
        current_user=current_user
    )