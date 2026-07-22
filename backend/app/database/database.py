from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import settings
from app.database.base import Base

from app.models.user import User
from app.models.resume import Resume
from app.models.resume_analysis import ResumeAnalysis
password = quote_plus(settings.DB_PASSWORD)

DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:"
    f"{password}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
