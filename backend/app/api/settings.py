from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user

from app.schemas.settings_schema import (
    SettingsResponse,
    SettingsUpdate,
    ChangePasswordRequest,
    MessageResponse
)

from app.services.settings_service import SettingsService


router = APIRouter(
    prefix="/settings",
    tags=["Settings"]
)


# -----------------------------------------
# Get Settings
# -----------------------------------------

@router.get(
    "/",
    response_model=SettingsResponse
)
def get_settings(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return SettingsService.get_settings(
        db=db,
        current_user=current_user
    )


# -----------------------------------------
# Update Settings
# -----------------------------------------

@router.put(
    "/",
    response_model=SettingsResponse
)
def update_settings(
    settings: SettingsUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return SettingsService.update_settings(
        db=db,
        settings_data=settings,
        current_user=current_user
    )


# -----------------------------------------
# Change Password
# -----------------------------------------

@router.put(
    "/change-password",
    response_model=MessageResponse
)
def change_password(
    password: ChangePasswordRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return SettingsService.change_password(
        db=db,
        password_data=password,
        current_user=current_user
    )


# -----------------------------------------
# Delete Account
# -----------------------------------------

@router.delete(
    "/account",
    response_model=MessageResponse
)
def delete_account(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return SettingsService.delete_account(
        db=db,
        current_user=current_user
    )