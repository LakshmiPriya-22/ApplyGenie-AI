from sqlalchemy.orm import Session

from app.models.profile import Profile


class ProfileRepository:

    # -------------------------------------
    # Create Profile
    # -------------------------------------

    @staticmethod
    def create(
        db: Session,
        user_id: int,
        profile_data
    ):

        profile = Profile(
            user_id=user_id,
            **profile_data.model_dump()
        )

        db.add(profile)
        db.commit()
        db.refresh(profile)

        return profile

    # -------------------------------------
    # Get By User ID
    # -------------------------------------

    @staticmethod
    def get_by_user_id(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Profile)
            .filter(Profile.user_id == user_id)
            .first()
        )

    # -------------------------------------
    # Get By Profile ID
    # -------------------------------------

    @staticmethod
    def get_by_id(
        db: Session,
        profile_id: int
    ):

        return (
            db.query(Profile)
            .filter(Profile.id == profile_id)
            .first()
        )

    # -------------------------------------
    # Update Profile
    # -------------------------------------

    @staticmethod
    def update(
        db: Session,
        profile: Profile,
        profile_data
    ):

        data = profile_data.model_dump(
            exclude_unset=True
        )

        for key, value in data.items():
            setattr(profile, key, value)

        db.commit()
        db.refresh(profile)

        return profile

    # -------------------------------------
    # Update Profile Image
    # -------------------------------------

    @staticmethod
    def update_profile_image(
        db: Session,
        profile: Profile,
        image_path: str
    ):

        profile.profile_image = image_path

        db.commit()
        db.refresh(profile)

        return profile

    # -------------------------------------
    # Delete Profile
    # -------------------------------------

    @staticmethod
    def delete(
        db: Session,
        profile: Profile
    ):

        db.delete(profile)
        db.commit()