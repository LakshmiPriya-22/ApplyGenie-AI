from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.schemas.email_schema import (
    EmailSendRequest,
    EmailResponse,
    EmailLogResponse,
    DeleteEmailLogResponse,
)

from app.services.email_service import EmailService

router = APIRouter(
    prefix="/emails",
    tags=["Email Automation"]
)


@router.post(
    "/send",
    response_model=EmailResponse
)
async def send_email(
    request: EmailSendRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return await EmailService.send_application_email(
        db=db,
        application_id=request.application_id,
        recipient_email=request.recipient_email,
        current_user=current_user
    )


@router.get(
    "",
    response_model=list[EmailLogResponse]
)
def get_email_logs(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return EmailService.get_my_email_logs(
        db=db,
        current_user=current_user
    )


@router.get(
    "/{email_log_id}",
    response_model=EmailLogResponse
)
def get_email_log(
    email_log_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return EmailService.get_email_log(
        db=db,
        email_log_id=email_log_id,
        current_user=current_user
    )


@router.delete(
    "/{email_log_id}",
    response_model=DeleteEmailLogResponse
)
def delete_email_log(
    email_log_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return EmailService.delete_email_log(
        db=db,
        email_log_id=email_log_id,
        current_user=current_user
    )