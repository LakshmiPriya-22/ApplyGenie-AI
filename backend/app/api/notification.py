from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user

from app.schemas.notification_schema import (
    NotificationCreate,
    NotificationResponse,
    NotificationReadResponse,
    NotificationDeleteResponse,
)

from app.services.notification_service import NotificationService

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"],
)


# -----------------------------------------
# Create Notification
# -----------------------------------------
@router.post(
    "/",
    response_model=NotificationResponse,
)
def create_notification(
    request: NotificationCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return NotificationService.create_notification(
        db=db,
        user_id=current_user.id,
        title=request.title,
        message=request.message,
        type=request.type,
    )


# -----------------------------------------
# Get All Notifications
# -----------------------------------------
@router.get(
    "/",
    response_model=list[NotificationResponse],
)
def get_notifications(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return NotificationService.get_notifications(
        db=db,
        current_user=current_user,
    )


# -----------------------------------------
# Get Unread Notifications
# -----------------------------------------
@router.get(
    "/unread",
    response_model=list[NotificationResponse],
)
def get_unread_notifications(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return NotificationService.get_unread_notifications(
        db=db,
        current_user=current_user,
    )


# -----------------------------------------
# Get Unread Count
# -----------------------------------------
@router.get("/count")
def get_unread_count(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return NotificationService.get_unread_count(
        db=db,
        current_user=current_user,
    )


# -----------------------------------------
# Mark One Notification as Read
# -----------------------------------------
@router.put(
    "/{notification_id}/read",
    response_model=NotificationReadResponse,
)
def mark_as_read(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return NotificationService.mark_as_read(
        db=db,
        notification_id=notification_id,
        current_user=current_user,
    )


# -----------------------------------------
# Mark All Notifications as Read
# -----------------------------------------
@router.put(
    "/read-all",
    response_model=NotificationReadResponse,
)
def mark_all_as_read(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return NotificationService.mark_all_as_read(
        db=db,
        current_user=current_user,
    )


# -----------------------------------------
# Delete Notification
# -----------------------------------------
@router.delete(
    "/{notification_id}",
    response_model=NotificationDeleteResponse,
)
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return NotificationService.delete_notification(
        db=db,
        notification_id=notification_id,
        current_user=current_user,
    )