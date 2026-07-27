from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.schemas.cover_letter_schema import (
    CoverLetterCreate,
    CoverLetterResponse,
    DeleteCoverLetterResponse,
)

from app.services.cover_letter_service import CoverLetterService

router = APIRouter(
    prefix="/cover-letters",
    tags=["AI Cover Letter"]
)


# ---------------------------------------
# Generate Cover Letter
# ---------------------------------------
@router.post(
    "/generate",
    response_model=CoverLetterResponse
)
def generate_cover_letter(
    request: CoverLetterCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return CoverLetterService.generate_cover_letter(
        db=db,
        resume_id=request.resume_id,
        job_id=request.job_id,
        current_user=current_user
    )


# ---------------------------------------
# Get My Cover Letters
# ---------------------------------------
@router.get(
    "",
    response_model=list[CoverLetterResponse]
)
def get_my_cover_letters(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return CoverLetterService.get_my_cover_letters(
        db=db,
        current_user=current_user
    )


# ---------------------------------------
# Get Cover Letter By ID
# ---------------------------------------
@router.get(
    "/{cover_letter_id}",
    response_model=CoverLetterResponse
)
def get_cover_letter(
    cover_letter_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return CoverLetterService.get_cover_letter(
        db=db,
        cover_letter_id=cover_letter_id,
        current_user=current_user
    )


# ---------------------------------------
# Delete Cover Letter
# ---------------------------------------
@router.delete(
    "/{cover_letter_id}",
    response_model=DeleteCoverLetterResponse
)
def delete_cover_letter(
    cover_letter_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return CoverLetterService.delete_cover_letter(
        db=db,
        cover_letter_id=cover_letter_id,
        current_user=current_user
    )