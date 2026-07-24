from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.logger import logger

from app.repositories.application_repository import ApplicationRepository
from app.repositories.resume_repository import ResumeRepository
from app.repositories.job_repository import JobRepository


class ApplicationService:

    @staticmethod
    def apply_job(
        db: Session,
        resume_id: int,
        job_id: int,
        current_user
    ):

        logger.info(
            f"User {current_user.id} applying for Job {job_id}"
        )

        resume = ResumeRepository.get_by_id(
            db=db,
            resume_id=resume_id
        )

        if not resume:
            raise HTTPException(
                status_code=404,
                detail="Resume not found."
            )

        if resume.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        job = JobRepository.get_job_by_id(
            db=db,
            job_id=job_id
        )

        if not job:
            raise HTTPException(
                status_code=404,
                detail="Job not found."
            )

        existing = ApplicationRepository.application_exists(
            db=db,
            user_id=current_user.id,
            resume_id=resume_id,
            job_id=job_id
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="You have already applied for this job."
            )

        application = ApplicationRepository.create_application(
            db=db,
            user_id=current_user.id,
            resume_id=resume_id,
            job_id=job_id
        )

        logger.info(
            f"Application {application.id} created successfully."
        )

        return application

    @staticmethod
    def get_my_applications(
        db: Session,
        current_user
    ):

        return ApplicationRepository.get_user_applications(
            db=db,
            user_id=current_user.id
        )

    @staticmethod
    def get_application(
        db: Session,
        application_id: int,
        current_user
    ):

        application = ApplicationRepository.get_application_by_id(
            db=db,
            application_id=application_id
        )

        if not application:
            raise HTTPException(
                status_code=404,
                detail="Application not found."
            )

        if application.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        return application

    @staticmethod
    def withdraw_application(
        db: Session,
        application_id: int,
        current_user
    ):

        application = ApplicationRepository.get_application_by_id(
            db=db,
            application_id=application_id
        )

        if not application:
            raise HTTPException(
                status_code=404,
                detail="Application not found."
            )

        if application.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        ApplicationRepository.delete_application(
            db=db,
            application=application
        )

        logger.info(
            f"Application {application_id} withdrawn."
        )

        return {
            "message": "Application withdrawn successfully."
        }

    @staticmethod
    def update_status(
        db: Session,
        application_id: int,
        status: str,
        recruiter_notes: str,
        current_user
    ):

        application = ApplicationRepository.get_application_by_id(
            db=db,
            application_id=application_id
        )

        if not application:
            raise HTTPException(
                status_code=404,
                detail="Application not found."
            )

        application = ApplicationRepository.update_status(
            db=db,
            application=application,
            status=status,
            recruiter_notes=recruiter_notes
        )

        logger.info(
            f"Application {application.id} updated."
        )

        return application

    @staticmethod
    def search_applications(
        db: Session,
        current_user,
        company: str | None = None,
        title: str | None = None,
        status: str | None = None,
        location: str | None = None,
        from_date: datetime | None = None,
        to_date: datetime | None = None
    ):

        logger.info(
            f"Searching applications for user {current_user.id}"
        )

        return ApplicationRepository.search_applications(
            db=db,
            user_id=current_user.id,
            company=company,
            title=title,
            status=status,
            location=location,
            from_date=from_date,
            to_date=to_date
        )