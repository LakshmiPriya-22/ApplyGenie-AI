from fastapi import FastAPI

from app.config.settings import settings

from app.database.database import engine

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)


@app.get("/")
def home():
    return {
        "message": "ApplyGenie AI Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }