from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.job_repository import JobRepository


class JobService:

    @staticmethod
    def create_job(
        db: Session,
        job,
        current_user
    ):
        job_data = job.model_dump()
        job_data["posted_by"] = current_user.id

        return JobRepository.create(
            db=db,
            job_data=job_data
        )

    @staticmethod
    def get_all_jobs(
        db: Session,
        page: int = 1,
        size: int = 10,
        company: str | None = None,
        location: str | None = None,
        employment_type: str | None = None,
        experience_level: str | None = None,
        skills: str | None = None,
        sort: str | None = None
    ):
        return JobRepository.get_all(db)

    @staticmethod
    def get_my_jobs(
        db: Session,
        current_user
    ):
        jobs = JobRepository.get_all(db)

        return [
            job
            for job in jobs
            if job.posted_by == current_user.id
        ]

    @staticmethod
    def get_job(
        db: Session,
        job_id: int
    ):
        job = JobRepository.get_by_id(
            db=db,
            job_id=job_id
        )

        if job is None:
            raise HTTPException(
                status_code=404,
                detail="Job not found."
            )

        return job

    @staticmethod
    def update_job(
        db: Session,
        job_id: int,
        job_update,
        current_user
    ):
        raise HTTPException(
            status_code=501,
            detail="Update not implemented."
        )

    @staticmethod
    def delete_job(
        db: Session,
        job_id: int,
        current_user
    ):
        job = JobRepository.get_by_id(
            db=db,
            job_id=job_id
        )

        if job is None:
            raise HTTPException(
                status_code=404,
                detail="Job not found."
            )

        JobRepository.delete(
            db=db,
            job=job
        )

        return {
            "message": "Job deleted successfully."
        }