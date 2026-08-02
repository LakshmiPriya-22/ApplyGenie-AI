from fastapi import HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models.user import User
from app.repositories.settings_repository import SettingsRepository
from app.services.notification_service import NotificationService


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


class SettingsService:

    # -----------------------------------------
    # Get Settings
    # -----------------------------------------

    @staticmethod
    def get_settings(
        db: Session,
        current_user
    ):

        settings = SettingsRepository.get_by_user_id(
            db=db,
            user_id=current_user.id
        )

        if settings:
            return settings

        return SettingsRepository.create(
            db=db,
            user_id=current_user.id
        )

    # -----------------------------------------
    # Update Settings
    # -----------------------------------------

    @staticmethod
    def update_settings(
        db: Session,
        settings_data,
        current_user
    ):

        settings = SettingsRepository.get_by_user_id(
            db=db,
            user_id=current_user.id
        )

        if not settings:
            settings = SettingsRepository.create(
                db=db,
                user_id=current_user.id
            )

        settings = SettingsRepository.update(
            db=db,
            settings=settings,
            settings_data=settings_data
        )

        NotificationService.create_notification(
            db=db,
            user_id=current_user.id,
            title="Settings Updated",
            message="Your account settings have been updated successfully.",
            type="INFO"
        )

        return settings

    # -----------------------------------------
    # Change Password
    # -----------------------------------------

    @staticmethod
    def change_password(
        db: Session,
        password_data,
        current_user
    ):

        user = (
            db.query(User)
            .filter(User.id == current_user.id)
            .first()
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

        if not pwd_context.verify(
            password_data.current_password,
            user.password
        ):
            raise HTTPException(
                status_code=400,
                detail="Current password is incorrect."
            )

        user.password = pwd_context.hash(
            password_data.new_password
        )

        db.commit()
        db.refresh(user)

        NotificationService.create_notification(
            db=db,
            user_id=current_user.id,
            title="Password Changed",
            message="Your password has been changed successfully.",
            type="SUCCESS"
        )

        return {
            "message": "Password changed successfully."
        }

    # -----------------------------------------
    # Delete Account
    # -----------------------------------------

    @staticmethod
    def delete_account(
        db: Session,
        current_user
    ):

        user = (
            db.query(User)
            .filter(User.id == current_user.id)
            .first()
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

        db.delete(user)
        db.commit()

        return {
            "message": "Account deleted successfully."
        }