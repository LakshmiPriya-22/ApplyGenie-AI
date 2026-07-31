from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.logger import logger
from app.repositories.job_repository import JobRepository


class JobService:

    @staticmethod
    def create_job(
        db: Session,
        job,
        current_user,
    ):
        logger.info(
            f"Creating job by user {current_user.id}"
        )

        job_data = job.model_dump()

        job_data["posted_by"] = current_user.id

        return JobRepository.create(
            db=db,
            job_data=job_data,
        )

    @staticmethod
    def get_all_jobs(
        db: Session,
        page: int = 1,
        size: int = 10,
        company=None,
        location=None,
        employment_type=None,
        experience_level=None,
        skills=None,
        sort=None,
    ):

        jobs = JobRepository.get_all(db)

        if company:
            jobs = [
                j for j in jobs
                if company.lower() in j.company.lower()
            ]

        if location:
            jobs = [
                j for j in jobs
                if j.location
                and location.lower() in j.location.lower()
            ]

        if employment_type:
            jobs = [
                j for j in jobs
                if j.employment_type == employment_type
            ]

        if experience_level:
            jobs = [
                j for j in jobs
                if j.experience_level == experience_level
            ]

        if skills:
            jobs = [
                j for j in jobs
                if j.skills
                and skills.lower() in j.skills.lower()
            ]

        if sort == "salary":
            jobs.sort(key=lambda x: x.salary or "")

        elif sort == "company":
            jobs.sort(key=lambda x: x.company)

        elif sort == "title":
            jobs.sort(key=lambda x: x.title)

        start = (page - 1) * size

        return jobs[start:start + size]

    @staticmethod
    def get_my_jobs(
        db: Session,
        current_user,
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
        job_id: int,
    ):

        job = JobRepository.get_by_id(
            db=db,
            job_id=job_id,
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
        current_user,
    ):

        job = JobRepository.get_by_id(
            db=db,
            job_id=job_id,
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

        return JobRepository.update(
            db=db,
            job=job,
            job_data=job_update.model_dump(
                exclude_unset=True
            )
        )

    @staticmethod
    def delete_job(
        db: Session,
        job_id: int,
        current_user,
    ):

        job = JobRepository.get_by_id(
            db=db,
            job_id=job_id,
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

        JobRepository.delete(
            db=db,
            job=job,
        )

        logger.info(
            f"Deleted job {job.id}"
        )

        return {
            "message": "Job deleted successfully."
        }