import os
import shutil
import uuid

from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.config.settings import settings

from app.repositories.profile_repository import ProfileRepository
from app.services.notification_service import NotificationService


UPLOAD_FOLDER = os.path.join(
    settings.UPLOAD_FOLDER,
    "profiles"
)


class ProfileService:

    # -----------------------------------------
    # Get Profile
    # -----------------------------------------

    @staticmethod
    def get_profile(
        db: Session,
        current_user
    ):

        profile = ProfileRepository.get_by_user_id(
            db=db,
            user_id=current_user.id
        )

        if profile:
            return profile

        # Create a default profile automatically
        profile_data = type(
            "ProfileData",
            (),
            {
                "model_dump": lambda self: {
                    "full_name": getattr(current_user, "name", current_user.email),
                    "phone": None,
                    "date_of_birth": None,
                    "gender": None,
                    "college": None,
                    "degree": None,
                    "branch": None,
                    "current_year": None,
                    "cgpa": None,
                    "headline": None,
                    "bio": None,
                    "skills": None,
                    "interests": None,
                    "linkedin": None,
                    "github": None,
                    "portfolio": None,
                }
            }
        )()

        profile = ProfileRepository.create(
            db=db,
            user_id=current_user.id,
            profile_data=profile_data
        )

        return profile

    # -----------------------------------------
    # Create Profile
    # -----------------------------------------

    @staticmethod
    def create_profile(
        db: Session,
        profile_data,
        current_user
    ):

        existing = ProfileRepository.get_by_user_id(
            db=db,
            user_id=current_user.id
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Profile already exists."
            )

        profile = ProfileRepository.create(
            db=db,
            user_id=current_user.id,
            profile_data=profile_data
        )

        NotificationService.create_notification(
            db=db,
            user_id=current_user.id,
            title="Profile Created",
            message="Your profile has been created successfully.",
            type="SUCCESS"
        )

        return profile

    # -----------------------------------------
    # Update Profile
    # -----------------------------------------

    @staticmethod
    def update_profile(
        db: Session,
        profile_data,
        current_user
    ):

        profile = ProfileRepository.get_by_user_id(
            db=db,
            user_id=current_user.id
        )

        if not profile:
            raise HTTPException(
                status_code=404,
                detail="Profile not found."
            )

        profile = ProfileRepository.update(
            db=db,
            profile=profile,
            profile_data=profile_data
        )

        NotificationService.create_notification(
            db=db,
            user_id=current_user.id,
            title="Profile Updated",
            message="Your profile has been updated successfully.",
            type="INFO"
        )

        return profile

    # -----------------------------------------
    # Upload Profile Image
    # -----------------------------------------

    @staticmethod
    def upload_profile_image(
        db: Session,
        file: UploadFile,
        current_user
    ):

        profile = ProfileRepository.get_by_user_id(
            db=db,
            user_id=current_user.id
        )

        if not profile:
            raise HTTPException(
                status_code=404,
                detail="Profile not found."
            )

        os.makedirs(
            UPLOAD_FOLDER,
            exist_ok=True
        )

        extension = file.filename.split(".")[-1]

        filename = (
            f"{uuid.uuid4()}.{extension}"
        )

        filepath = os.path.join(
            UPLOAD_FOLDER,
            filename
        )

        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        profile = ProfileRepository.update_profile_image(
            db=db,
            profile=profile,
            image_path=filepath
        )

        NotificationService.create_notification(
            db=db,
            user_id=current_user.id,
            title="Profile Picture Updated",
            message="Your profile picture has been updated.",
            type="SUCCESS"
        )

        return profile

    # -----------------------------------------
    # Delete Profile Image
    # -----------------------------------------

    @staticmethod
    def delete_profile_image(
        db: Session,
        current_user
    ):

        profile = ProfileRepository.get_by_user_id(
            db=db,
            user_id=current_user.id
        )

        if not profile:
            raise HTTPException(
                status_code=404,
                detail="Profile not found."
            )

        if profile.profile_image and os.path.exists(
            profile.profile_image
        ):
            os.remove(
                profile.profile_image
            )

        profile = ProfileRepository.update_profile_image(
            db=db,
            profile=profile,
            image_path=None
        )

        NotificationService.create_notification(
            db=db,
            user_id=current_user.id,
            title="Profile Picture Removed",
            message="Your profile picture has been removed.",
            type="INFO"
        )

        return {
            "message": "Profile picture removed successfully."
        }

    # -----------------------------------------
    # Delete Profile
    # -----------------------------------------

    @staticmethod
    def delete_profile(
        db: Session,
        current_user
    ):

        profile = ProfileRepository.get_by_user_id(
            db=db,
            user_id=current_user.id
        )

        if not profile:
            raise HTTPException(
                status_code=404,
                detail="Profile not found."
            )

        if profile.profile_image and os.path.exists(
            profile.profile_image
        ):
            os.remove(
                profile.profile_image
            )

        ProfileRepository.delete(
            db=db,
            profile=profile
        )

        NotificationService.create_notification(
            db=db,
            user_id=current_user.id,
            title="Profile Deleted",
            message="Your profile has been deleted.",
            type="WARNING"
        )

        return {
            "message": "Profile deleted successfully."
        }