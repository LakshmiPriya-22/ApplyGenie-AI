from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.notification_repository import (
    NotificationRepository,
)


class NotificationService:

    # -----------------------------------------
    # Create Notification
    # -----------------------------------------
    @staticmethod
    def create_notification(
        db: Session,
        user_id: int,
        title: str,
        message: str,
        type: str = "INFO",
    ):

        return NotificationRepository.create(
            db=db,
            user_id=user_id,
            title=title,
            message=message,
            type=type,
        )

    # -----------------------------------------
    # Get All Notifications
    # -----------------------------------------
    @staticmethod
    def get_notifications(
        db: Session,
        current_user,
    ):

        return NotificationRepository.get_all_by_user(
            db=db,
            user_id=current_user.id,
        )

    # -----------------------------------------
    # Get Unread Notifications
    # -----------------------------------------
    @staticmethod
    def get_unread_notifications(
        db: Session,
        current_user,
    ):

        return NotificationRepository.get_unread(
            db=db,
            user_id=current_user.id,
        )

    # -----------------------------------------
    # Count Unread Notifications
    # -----------------------------------------
    @staticmethod
    def get_unread_count(
        db: Session,
        current_user,
    ):

        return {
            "unread": NotificationRepository.count_unread(
                db=db,
                user_id=current_user.id,
            )
        }

    # -----------------------------------------
    # Mark Notification as Read
    # -----------------------------------------
    @staticmethod
    def mark_as_read(
        db: Session,
        notification_id: int,
        current_user,
    ):

        notification = NotificationRepository.get_by_id(
            db=db,
            notification_id=notification_id,
        )

        if not notification:
            raise HTTPException(
                status_code=404,
                detail="Notification not found.",
            )

        if notification.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied.",
            )

        NotificationRepository.mark_as_read(
            db=db,
            notification=notification,
        )

        return {
            "message": "Notification marked as read."
        }

    # -----------------------------------------
    # Mark All Notifications as Read
    # -----------------------------------------
    @staticmethod
    def mark_all_as_read(
        db: Session,
        current_user,
    ):

        NotificationRepository.mark_all_as_read(
            db=db,
            user_id=current_user.id,
        )

        return {
            "message": "All notifications marked as read."
        }

    # -----------------------------------------
    # Delete Notification
    # -----------------------------------------
    @staticmethod
    def delete_notification(
        db: Session,
        notification_id: int,
        current_user,
    ):

        notification = NotificationRepository.get_by_id(
            db=db,
            notification_id=notification_id,
        )

        if not notification:
            raise HTTPException(
                status_code=404,
                detail="Notification not found.",
            )

        if notification.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied.",
            )

        NotificationRepository.delete(
            db=db,
            notification=notification,
        )

        return {
            "message": "Notification deleted successfully."
        }