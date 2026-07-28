from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.resume import router as resume_router
from app.api.analyzer import router as analyzer_router
from app.api.job import router as job_router
from app.api.job_match import router as job_match_router
from app.api.recommendation import router as recommendation_router
from app.api.application import router as application_router
from app.api.interview import router as interview_router
from app.api.cover_letter import router as cover_letter_router
from app.api.email import router as email_router
from app.api.resume_chat import router as resume_chat_router
from app.api.dashboard import router as dashboard_router
from app.api.analytics import router as analytics_router
from app.api.resume_optimizer import router as resume_optimizer_router
from app.api.resume_pdf import router as resume_pdf_router
from app.api.job_discovery import router as job_discovery_router
from app.api import interview_schedule

from app.core.exception_handlers import register_exception_handlers

# Create FastAPI app FIRST
app = FastAPI(
    title="ApplyGenie AI",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register exception handlers
register_exception_handlers(app)

# Register routers
app.include_router(auth_router)
app.include_router(resume_router)
app.include_router(analyzer_router)
app.include_router(job_router)
app.include_router(job_match_router)
app.include_router(recommendation_router)
app.include_router(application_router)
app.include_router(interview_router)
app.include_router(cover_letter_router)
app.include_router(email_router)
app.include_router(dashboard_router)
app.include_router(analytics_router)
app.include_router(interview_schedule.router)
app.include_router(resume_chat_router)
app.include_router(resume_optimizer_router)
app.include_router(resume_pdf_router)
app.include_router(job_discovery_router)