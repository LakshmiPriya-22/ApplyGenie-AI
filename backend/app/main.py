from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.resume import router as resume_router
from app.api.analyzer import router as analyzer_router
from app.api.job import router as job_router
from app.api.job_match import router as job_match_router

from app.api.recommendation import router as recommendation_router

from app.api.application import router as application_router
from app.api.interview import router as interview_router



from app.core.exception_handlers import (
    register_exception_handlers
)

app = FastAPI(
    title="ApplyGenie AI",
    version="1.0.0"
)

register_exception_handlers(app)

app.include_router(auth_router)
app.include_router(resume_router)
app.include_router(analyzer_router)
app.include_router(job_router)
app.include_router(job_match_router)
app.include_router(recommendation_router)
app.include_router(application_router)
app.include_router(interview_router)