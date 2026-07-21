from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.logger import logger
from app.repositories.job_repository import JobRepository
from app.schemas.job_schema import (
    JobCreate,
    JobUpdate
)


class JobService:

    @staticmethod
    def create_job(
        db: Session,
        job: JobCreate,
        current_user
    ):

        logger.info(
            f"User {current_user.id} is creating a new job."
        )

        created_job = JobRepository.create_job(
            db=db,
            job=job,
            user_id=current_user.id
        )

        logger.info(
            f"Job {created_job.id} created successfully."
        )

        return created_job

    @staticmethod
    def get_all_jobs(
        db: Session
    ):

        logger.info("Fetching all jobs.")

        return JobRepository.get_all_jobs(db)

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
            logger.error(
                f"Job {job_id} not found."
            )

            raise HTTPException(
                status_code=404,
                detail="Job not found."
            )

        return job

    @staticmethod
    def get_my_jobs(
        db: Session,
        current_user
    ):

        logger.info(
            f"Fetching jobs of user {current_user.id}"
        )

        return JobRepository.get_jobs_by_user(
            db=db,
            user_id=current_user.id
        )

    @staticmethod
    def update_job(
        db: Session,
        job_id: int,
        job_update: JobUpdate,
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

        updated_job = JobRepository.update_job(
            db=db,
            job=job,
            job_update=job_update
        )

        logger.info(
            f"Job {job.id} updated successfully."
        )

        return updated_job

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
            f"Job {job.id} deleted successfully."
        )

        return {
            "message": "Job deleted successfully."
        }