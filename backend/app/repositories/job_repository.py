from sqlalchemy.orm import Session

from app.models.job import Job
from app.schemas.job_schema import JobCreate, JobUpdate


class JobRepository:

    @staticmethod
    def create_job(
        db: Session,
        job: JobCreate,
        user_id: int
    ):

        new_job = Job(
            title=job.title,
            company=job.company,
            location=job.location,
            employment_type=job.employment_type,
            experience_level=job.experience_level,
            salary=job.salary,
            description=job.description,
            requirements=job.requirements,
            skills=job.skills,
            posted_by=user_id
        )

        db.add(new_job)
        db.commit()
        db.refresh(new_job)

        return new_job

    @staticmethod
    def get_all_jobs(
        db: Session
    ):
        return (
            db.query(Job)
            .order_by(Job.created_at.desc())
            .all()
        )

    @staticmethod
    def get_job_by_id(
        db: Session,
        job_id: int
    ):
        return (
            db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )

    @staticmethod
    def get_jobs_by_user(
        db: Session,
        user_id: int
    ):
        return (
            db.query(Job)
            .filter(Job.posted_by == user_id)
            .order_by(Job.created_at.desc())
            .all()
        )

    @staticmethod
    def update_job(
        db: Session,
        job: Job,
        job_update: JobUpdate
    ):

        update_data = job_update.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(job, key, value)

        db.commit()
        db.refresh(job)

        return job

    @staticmethod
    def delete_job(
        db: Session,
        job: Job
    ):

        db.delete(job)
        db.commit()