from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func

from app.models.application import Application
from app.models.job import Job


class ApplicationRepository:

    @staticmethod
    def create_application(db: Session, user_id: int, resume_id: int, job_id: int):

        application = Application(user_id=user_id, resume_id=resume_id, job_id=job_id)

        db.add(application)
        db.commit()
        db.refresh(application)

        return application

    @staticmethod
    def get_application_by_id(db: Session, application_id: int):

        return (
            db.query(Application)
            .options(joinedload(Application.job))
            .filter(Application.id == application_id)
            .first()
        )

    @staticmethod
    def get_user_applications(db: Session, user_id: int):

        return (
            db.query(Application)
            .options(joinedload(Application.job))
            .filter(Application.user_id == user_id)
            .order_by(Application.applied_at.desc())
            .all()
        )

    @staticmethod
    def get_application_by_job_and_resume(db: Session, resume_id: int, job_id: int):

        return (
            db.query(Application)
            .filter(Application.resume_id == resume_id, Application.job_id == job_id)
            .first()
        )

    @staticmethod
    def update_status(
<<<<<<< Updated upstream
        db: Session,
        application: Application,
        status: str,
        recruiter_notes: str | None = None
=======
        db: Session, application: Application, status: str, notes: str | None = None
>>>>>>> Stashed changes
    ):

        application.status = status
        application.recruiter_notes = recruiter_notes

        db.commit()
        db.refresh(application)

        return application

    @staticmethod
    def delete_application(db: Session, application: Application):

        db.delete(application)
        db.commit()

    @staticmethod
    def get_job_applications(db: Session, job_id: int):

        return (
            db.query(Application)
            .filter(Application.job_id == job_id)
            .order_by(Application.applied_at.desc())
            .all()
        )

    @staticmethod
    def get_resume_applications(db: Session, resume_id: int):

        return (
            db.query(Application)
            .filter(Application.resume_id == resume_id)
            .order_by(Application.applied_at.desc())
            .all()
        )

    @staticmethod
    def application_exists(db: Session, user_id: int, resume_id: int, job_id: int):

        return (
            db.query(Application)
            .filter(
                Application.user_id == user_id,
                Application.resume_id == resume_id,
                Application.job_id == job_id,
            )
            .first()
        )

    @staticmethod
    def search_applications(
        db: Session,
        user_id: int,
        company: str | None = None,
        title: str | None = None,
        status: str | None = None,
        location: str | None = None,
        from_date=None,
        to_date=None,
    ):

        query = (
            db.query(Application)
            .options(joinedload(Application.job))
            .join(Job, Application.job_id == Job.id)
            .filter(Application.user_id == user_id)
        )

        if company:
            query = query.filter(Job.company.ilike(f"%{company}%"))

        if title:
            query = query.filter(Job.title.ilike(f"%{title}%"))

        if status:
            query = query.filter(Application.status == status)

        if location:
            query = query.filter(Job.location.ilike(f"%{location}%"))

        if from_date:
            query = query.filter(Application.applied_at >= from_date)

        if to_date:
            query = query.filter(Application.applied_at <= to_date)

        return query.order_by(Application.applied_at.desc()).all()

    @staticmethod
    def get_dashboard_statistics(db: Session, user_id: int):

        stats = (
            db.query(Application.status, func.count(Application.id))
            .filter(Application.user_id == user_id)
            .group_by(Application.status)
            .all()
        )

        dashboard = {
            "total": 0,
            "applied": 0,
            "screening": 0,
            "interview": 0,
            "assessment": 0,
            "offer": 0,
            "rejected": 0,
            "withdrawn": 0,
        }

        for status, count in stats:

            dashboard["total"] += count

            key = status.lower()

            if key in dashboard:
                dashboard[key] = count

        return dashboard
