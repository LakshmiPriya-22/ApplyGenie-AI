from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    InvalidPDFException,
    FileTooLargeException,
    ResumeNotFoundException,
    ResumeAnalysisNotFoundException
)
from app.core.logger import logger


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(InvalidPDFException)
    async def invalid_pdf_handler(
        request: Request,
        exc: InvalidPDFException
    ):

        logger.error(
            f"Invalid PDF Exception: {exc.message}"
        )

        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": exc.message
            }
        )

    @app.exception_handler(FileTooLargeException)
    async def file_size_handler(
        request: Request,
        exc: FileTooLargeException
    ):

        logger.error(
            f"File Too Large Exception: {exc.message}"
        )

        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": exc.message
            }
        )

    @app.exception_handler(ResumeNotFoundException)
    async def resume_handler(
        request: Request,
        exc: ResumeNotFoundException
    ):

        logger.error(
            f"Resume Not Found Exception: {exc.message}"
        )

        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": exc.message
            }
        )

    @app.exception_handler(ResumeAnalysisNotFoundException)
    async def analysis_handler(
        request: Request,
        exc: ResumeAnalysisNotFoundException
    ):

        logger.error(
            f"Resume Analysis Not Found Exception: {exc.message}"
        )

        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": exc.message
            }
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception
    ):

        logger.exception(
            f"Unhandled Exception: {str(exc)}"
        )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Internal Server Error"
            }
        )