from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File
)
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user

from app.schemas.profile_schema import (
    ProfileCreate,
    ProfileUpdate,
    ProfileResponse
)

from app.services.profile_service import ProfileService


router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


# -----------------------------------------
# Get Profile
# -----------------------------------------

@router.get(
    "/",
    response_model=ProfileResponse
)
def get_profile(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ProfileService.get_profile(
        db=db,
        current_user=current_user
    )


# -----------------------------------------
# Create Profile
# -----------------------------------------

@router.post(
    "/",
    response_model=ProfileResponse
)
def create_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ProfileService.create_profile(
        db=db,
        profile_data=profile,
        current_user=current_user
    )


# -----------------------------------------
# Update Profile
# -----------------------------------------

@router.put(
    "/",
    response_model=ProfileResponse
)
def update_profile(
    profile: ProfileUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ProfileService.update_profile(
        db=db,
        profile_data=profile,
        current_user=current_user
    )


# -----------------------------------------
# Upload Profile Image
# -----------------------------------------

@router.post(
    "/photo",
    response_model=ProfileResponse
)
def upload_profile_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ProfileService.upload_profile_image(
        db=db,
        file=file,
        current_user=current_user
    )


# -----------------------------------------
# Delete Profile Image
# -----------------------------------------

@router.delete("/photo")
def delete_profile_image(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ProfileService.delete_profile_image(
        db=db,
        current_user=current_user
    )


# -----------------------------------------
# Delete Profile
# -----------------------------------------

@router.delete("/")
def delete_profile(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return ProfileService.delete_profile(
        db=db,
        current_user=current_user
    )