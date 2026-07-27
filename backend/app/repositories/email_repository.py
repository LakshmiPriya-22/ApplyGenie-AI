from datetime import datetime

from sqlalchemy.orm import Session

from app.models.email_log import EmailLog


class EmailRepository:

    @staticmethod
    def create_email_log(
        db: Session,
        user_id: int,
        application_id: int,
        recipient_email: str,
        subject: str
    ):

        email_log = EmailLog(
            user_id=user_id,
            application_id=application_id,
            recipient_email=recipient_email,
            subject=subject,
            status="Pending"
        )

        db.add(email_log)
        db.commit()
        db.refresh(email_log)

        return email_log

    @staticmethod
    def get_email_log_by_id(
        db: Session,
        email_log_id: int
    ):

        return (
            db.query(EmailLog)
            .filter(EmailLog.id == email_log_id)
            .first()
        )

    @staticmethod
    def get_user_email_logs(
        db: Session,
        user_id: int
    ):

        return (
            db.query(EmailLog)
            .filter(EmailLog.user_id == user_id)
            .order_by(EmailLog.created_at.desc())
            .all()
        )

    @staticmethod
    def update_email_status(
        db: Session,
        email_log: EmailLog,
        status: str,
        error_message: str = None
    ):

        email_log.status = status
        email_log.error_message = error_message

        if status == "Sent":
            email_log.sent_at = datetime.utcnow()

        db.commit()
        db.refresh(email_log)

        return email_log

    @staticmethod
    def delete_email_log(
        db: Session,
        email_log: EmailLog
    ):

        db.delete(email_log)
        db.commit()

    @staticmethod
    def email_log_exists(
        db: Session,
        application_id: int,
        recipient_email: str
    ):

        return (
            db.query(EmailLog)
            .filter(
                EmailLog.application_id == application_id,
                EmailLog.recipient_email == recipient_email
            )
            .first()
        )