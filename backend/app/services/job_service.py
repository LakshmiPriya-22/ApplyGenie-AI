from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.logger import logger

from app.repositories.job_repository import JobRepository


class JobService:

    @staticmethod
    def create_job(
        db: Session,
        job,
        current_user
    ):

        logger.info(
            f"Creating job by user {current_user.id}"
        )

        return JobRepository.create_job(
            db=db,
            job=job,
            user_id=current_user.id
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

        return JobRepository.get_all_jobs(
            db=db,
            page=page,
            size=size,
            company=company,
            location=location,
            employment_type=employment_type,
            experience_level=experience_level,
            skills=skills,
            sort=sort
        )

    @staticmethod
    def get_my_jobs(
        db: Session,
        current_user
    ):

        return JobRepository.get_jobs_by_user(
            db=db,
            user_id=current_user.id
        )

    @staticmethod
    def get_job(
        db: Session,
        job_id: int
    ):

        job = JobRepository.get_job_by_id(
            db=db,
            job_id=job_id
        )

        if not job:
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

        job = JobRepository.get_job_by_id(
            db=db,
            job_id=job_id
        )

        if not job:
            raise HTTPException(
                status_code=404,
                detail="Job not found."
            )

        if job.posted_by != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        logger.info(
            f"Updating job {job.id}"
        )

        return JobRepository.update_job(
            db=db,
            job=job,
            job_update=job_update
        )

    @staticmethod
    def delete_job(
        db: Session,
        job_id: int,
        current_user
    ):

        job = JobRepository.get_job_by_id(
            db=db,
            job_id=job_id
        )

        if not job:
            raise HTTPException(
                status_code=404,
                detail="Job not found."
            )

        if job.posted_by != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        JobRepository.delete_job(
            db=db,
            job=job
        )

        logger.info(
            f"Deleted job {job.id}"
        )

        return {
            "message": "Job deleted successfully."
        }