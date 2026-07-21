import os
import shutil
import uuid

from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.config.settings import settings
from app.core.exceptions import (
    InvalidPDFException,
    FileTooLargeException
)
from app.core.logger import logger
from app.repositories.resume_repository import ResumeRepository
from app.repositories.resume_analysis_repository import ResumeAnalysisRepository
from app.services.resume_analysis_service import ResumeAnalysisService
from app.utils.pdf_parser import extract_text_from_pdf

UPLOAD_FOLDER = settings.UPLOAD_FOLDER


class ResumeService:

    @staticmethod
    def upload_resume(
        db: Session,
        file: UploadFile,
        current_user
    ):

        logger.info(
            f"Resume upload started by user {current_user.id}"
        )

        if file.content_type != "application/pdf":
            raise InvalidPDFException()

        file.file.seek(0, os.SEEK_END)
        file_size = file.file.tell()
        file.file.seek(0)

        if file_size > settings.MAX_FILE_SIZE:
            raise FileTooLargeException()

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        unique_filename = f"{uuid.uuid4()}_{file.filename}"

        filepath = os.path.join(
            UPLOAD_FOLDER,
            unique_filename
        )

        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        extracted_text = extract_text_from_pdf(filepath)

        resume = ResumeRepository.create_resume(
            db=db,
            filename=unique_filename,
            filepath=filepath,
            extracted_text=extracted_text,
            user_id=current_user.id
        )

        ResumeAnalysisService.generate_analysis(
            db=db,
            resume=resume
        )

        logger.info(
            f"Resume uploaded successfully : {resume.id}"
        )

        return {
            "message": "Resume uploaded successfully.",
            "resume_id": resume.id,
            "filename": resume.filename
        }

    @staticmethod
    def get_all_resumes(
        db: Session,
        current_user
    ):
        return ResumeRepository.get_all_by_user(
            db=db,
            user_id=current_user.id
        )

    @staticmethod
    def get_resume(
        db: Session,
        resume_id: int,
        current_user
    ):

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

        return resume

    @staticmethod
    def delete_resume(
        db: Session,
        resume_id: int,
        current_user
    ):

        resume = ResumeService.get_resume(
            db=db,
            resume_id=resume_id,
            current_user=current_user
        )

        # Delete AI analysis first
        analysis = ResumeAnalysisRepository.get_by_resume_id(
            db=db,
            resume_id=resume.id
        )

        if analysis:
            ResumeAnalysisRepository.delete(
                db=db,
                analysis=analysis
            )

        # Delete PDF file
        if os.path.exists(resume.filepath):
            os.remove(resume.filepath)

        # Delete resume record
        ResumeRepository.delete(
            db=db,
            resume=resume
        )

        logger.info(
            f"Resume {resume.id} deleted successfully."
        )

        return {
            "message": "Resume deleted successfully."
        }