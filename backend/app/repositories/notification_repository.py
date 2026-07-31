from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.models.notification import Notification


class NotificationRepository:

    # -----------------------------------------
    # Create Notification
    # -----------------------------------------
    @staticmethod
    def create(
        db: Session,
        user_id: int,
        title: str,
        message: str,
        type: str = "INFO"
    ):

        notification = Notification(
            user_id=user_id,
            title=title,
            message=message,
            type=type
        )

        db.add(notification)
        db.commit()
        db.refresh(notification)

        return notification

    # -----------------------------------------
    # Get All Notifications of User
    # -----------------------------------------
    @staticmethod
    def get_all_by_user(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Notification)
            .filter(
                Notification.user_id == user_id
            )
            .order_by(
                desc(Notification.created_at)
            )
            .all()
        )

    # -----------------------------------------
    # Get Notification By ID
    # -----------------------------------------
    @staticmethod
    def get_by_id(
        db: Session,
        notification_id: int
    ):

        return (
            db.query(Notification)
            .filter(
                Notification.id == notification_id
            )
            .first()
        )

    # -----------------------------------------
    # Get Unread Notifications
    # -----------------------------------------
    @staticmethod
    def get_unread(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Notification)
            .filter(
                Notification.user_id == user_id,
                Notification.is_read == False
            )
            .order_by(
                desc(Notification.created_at)
            )
            .all()
        )

    # -----------------------------------------
    # Count Unread Notifications
    # -----------------------------------------
    @staticmethod
    def count_unread(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Notification)
            .filter(
                Notification.user_id == user_id,
                Notification.is_read == False
            )
            .count()
        )

    # -----------------------------------------
    # Mark One Notification as Read
    # -----------------------------------------
    @staticmethod
    def mark_as_read(
        db: Session,
        notification: Notification
    ):

        notification.is_read = True

        db.commit()
        db.refresh(notification)

        return notification

    # -----------------------------------------
    # Mark All Notifications as Read
    # -----------------------------------------
    @staticmethod
    def mark_all_as_read(
        db: Session,
        user_id: int
    ):

        notifications = (
            db.query(Notification)
            .filter(
                Notification.user_id == user_id,
                Notification.is_read == False
            )
            .all()
        )

        for notification in notifications:
            notification.is_read = True

        db.commit()

        return notifications

    # -----------------------------------------
    # Delete Notification
    # -----------------------------------------
    @staticmethod
    def delete(
        db: Session,
        notification: Notification
    ):

        db.delete(notification)
        db.commit()