from sqlalchemy.orm import Session

from app.models.settings import Settings


class SettingsRepository:

    # -----------------------------------------
    # Create Settings
    # -----------------------------------------

    @staticmethod
    def create(
        db: Session,
        user_id: int
    ):

        settings = Settings(
            user_id=user_id
        )

        db.add(settings)
        db.commit()
        db.refresh(settings)

        return settings

    # -----------------------------------------
    # Get By User ID
    # -----------------------------------------

    @staticmethod
    def get_by_user_id(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Settings)
            .filter(Settings.user_id == user_id)
            .first()
        )

    # -----------------------------------------
    # Get By ID
    # -----------------------------------------

    @staticmethod
    def get_by_id(
        db: Session,
        settings_id: int
    ):

        return (
            db.query(Settings)
            .filter(Settings.id == settings_id)
            .first()
        )

    # -----------------------------------------
    # Update Settings
    # -----------------------------------------

    @staticmethod
    def update(
        db: Session,
        settings: Settings,
        settings_data
    ):

        data = settings_data.model_dump(
            exclude_unset=True
        )

        for key, value in data.items():
            setattr(
                settings,
                key,
                value
            )

        db.commit()
        db.refresh(settings)

        return settings

    # -----------------------------------------
    # Delete Settings
    # -----------------------------------------

    @staticmethod
    def delete(
        db: Session,
        settings: Settings
    ):

        db.delete(settings)
        db.commit()