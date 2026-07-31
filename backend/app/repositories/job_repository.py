from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.models.job import Job


class JobRepository:

    @staticmethod
    def create(
        db: Session,
        job_data: dict,
    ):
        job = Job(**job_data)

        db.add(job)
        db.commit()
        db.refresh(job)

        return job

    @staticmethod
    def get_all(
        db: Session,
    ):
        return (
            db.query(Job)
            .order_by(desc(Job.created_at))
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        job_id: int,
    ):
        return (
            db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        job: Job,
        job_data: dict,
    ):
        for key, value in job_data.items():
            setattr(job, key, value)

        db.commit()
        db.refresh(job)

        return job

    @staticmethod
    def delete(
        db: Session,
        job: Job,
    ):
        db.delete(job)
        db.commit()

    @staticmethod
    def count(
        db: Session,
    ):
        return db.query(Job).count()

    @staticmethod
    def get_by_title_company(
        db: Session,
        title: str,
        company: str,
    ):
        return (
            db.query(Job)
            .filter(
                Job.title == title,
                Job.company == company
            )
            .first()
        )