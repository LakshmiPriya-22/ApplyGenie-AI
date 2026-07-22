from pathlib import Path

from fastapi import HTTPException
from fastapi_mail import FastMail, MessageSchema, MessageType
from sqlalchemy.orm import Session

from app.core.logger import logger
from app.core.mail import conf

from app.repositories.application_repository import ApplicationRepository
from app.repositories.cover_letter_repository import CoverLetterRepository
from app.repositories.email_repository import EmailRepository


class EmailService:

    @staticmethod
    async def send_application_email(
        db: Session,
        application_id: int,
        recipient_email: str,
        current_user
    ):

        # -----------------------------
        # Verify Application
        # -----------------------------
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

        # -----------------------------
        # Resume
        # -----------------------------
        resume = application.resume

        if not resume:
            raise HTTPException(
                status_code=404,
                detail="Resume not found."
            )

        # -----------------------------
        # Cover Letter
        # -----------------------------
        cover_letter = CoverLetterRepository.get_cover_letter_by_resume_and_job(
            db=db,
            resume_id=resume.id,
            job_id=application.job_id
        )

        if not cover_letter:
            raise HTTPException(
                status_code=404,
                detail="Generate a cover letter first."
            )

        # -----------------------------
        # Create Email Log
        # -----------------------------
        subject = f"Application for {application.job.title}"

        email_log = EmailRepository.create_email_log(
            db=db,
            user_id=current_user.id,
            application_id=application.id,
            recipient_email=recipient_email,
            subject=subject
        )

        # -----------------------------
        # Resume Attachment
        # -----------------------------
        resume_path = Path(resume.filepath)

        if not resume_path.exists():
            raise HTTPException(
                status_code=404,
                detail="Resume PDF not found."
            )

        body = f"""
        Dear Hiring Manager,

        {cover_letter.content}

        Regards,
        {current_user.email}
        """

        message = MessageSchema(
            subject=subject,
            recipients=[recipient_email],
            body=body,
            subtype=MessageType.html,
            attachments=[
                str(resume_path)
            ]
        )

        fm = FastMail(conf)

        try:

            await fm.send_message(message)

            EmailRepository.update_email_status(
                db=db,
                email_log=email_log,
                status="Sent"
            )

            logger.info("Email sent successfully.")

            return {
                "message": "Email sent successfully.",
                "status": "Sent"
            }

        except Exception as e:

            logger.exception(e)

            EmailRepository.update_email_status(
                db=db,
                email_log=email_log,
                status="Failed",
                error_message=str(e)
            )

            raise HTTPException(
                status_code=500,
                detail="Failed to send email."
            )

    @staticmethod
    def get_my_email_logs(
        db: Session,
        current_user
    ):

        return EmailRepository.get_user_email_logs(
            db=db,
            user_id=current_user.id
        )

    @staticmethod
    def get_email_log(
        db: Session,
        email_log_id: int,
        current_user
    ):

        email_log = EmailRepository.get_email_log_by_id(
            db=db,
            email_log_id=email_log_id
        )

        if not email_log:
            raise HTTPException(
                status_code=404,
                detail="Email log not found."
            )

        if email_log.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        return email_log

    @staticmethod
    def delete_email_log(
        db: Session,
        email_log_id: int,
        current_user
    ):

        email_log = EmailRepository.get_email_log_by_id(
            db=db,
            email_log_id=email_log_id
        )

        if not email_log:
            raise HTTPException(
                status_code=404,
                detail="Email log not found."
            )

        if email_log.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied."
            )

        EmailRepository.delete_email_log(
            db=db,
            email_log=email_log
        )

        return {
            "message": "Email log deleted successfully."
        }