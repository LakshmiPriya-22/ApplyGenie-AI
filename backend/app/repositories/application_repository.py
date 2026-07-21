from sqlalchemy.orm import Session

from app.models.application import Application


class ApplicationRepository:

    @staticmethod
    def create_application(
        db: Session,
        user_id: int,
        resume_id: int,
        job_id: int
    ):

        application = Application(
            user_id=user_id,
            resume_id=resume_id,
            job_id=job_id
        )

        db.add(application)
        db.commit()
        db.refresh(application)

        return application

    @staticmethod
    def get_application_by_id(
        db: Session,
        application_id: int
    ):

        return (
            db.query(Application)
            .filter(Application.id == application_id)
            .first()
        )

    @staticmethod
    def get_user_applications(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Application)
            .filter(Application.user_id == user_id)
            .order_by(Application.applied_at.desc())
            .all()
        )

    @staticmethod
    def get_application_by_job_and_resume(
        db: Session,
        resume_id: int,
        job_id: int
    ):

        return (
            db.query(Application)
            .filter(
                Application.resume_id == resume_id,
                Application.job_id == job_id
            )
            .first()
        )

    @staticmethod
    def update_status(
        db: Session,
        application: Application,
        status: str,
        recruiter_notes: str | None = None
    ):

        application.status = status
        application.recruiter_notes = recruiter_notes

        db.commit()
        db.refresh(application)

        return application

    @staticmethod
    def delete_application(
        db: Session,
        application: Application
    ):

        db.delete(application)
        db.commit()

    @staticmethod
    def get_job_applications(
        db: Session,
        job_id: int
    ):

        return (
            db.query(Application)
            .filter(Application.job_id == job_id)
            .order_by(Application.applied_at.desc())
            .all()
        )

    @staticmethod
    def get_resume_applications(
        db: Session,
        resume_id: int
    ):

        return (
            db.query(Application)
            .filter(Application.resume_id == resume_id)
            .order_by(Application.applied_at.desc())
            .all()
        )

    @staticmethod
    def application_exists(
        db: Session,
        user_id: int,
        resume_id: int,
        job_id: int
    ):

        return (
            db.query(Application)
            .filter(
                Application.user_id == user_id,
                Application.resume_id == resume_id,
                Application.job_id == job_id
            )
            .first()
        )