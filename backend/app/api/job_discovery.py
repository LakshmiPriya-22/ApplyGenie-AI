from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user

from app.agents.job_discovery_agent import JobDiscoveryAgent


router = APIRouter(
    prefix="/jobs",
    tags=["Job Discovery"]
)


@router.post("/discover")
def discover_jobs(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Manually trigger the Job Discovery Agent.
    """

    agent = JobDiscoveryAgent()

    result = agent.discover_jobs(db)

    return {
        "message": "Job discovery completed successfully.",
        "statistics": result
    }