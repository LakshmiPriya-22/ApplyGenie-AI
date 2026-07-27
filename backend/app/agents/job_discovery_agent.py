from sqlalchemy.orm import Session

from app.providers.provider_manager import ProviderManager
from app.services.job_discovery_service import JobDiscoveryService
from app.providers.greenhouse_provider import GreenhouseProvider


class JobDiscoveryAgent:

    def __init__(self):

        self.provider_manager = ProviderManager()

    def discover_jobs(
        self,
        db: Session
    ):

        discovered_jobs = (
            self.provider_manager.discover_jobs()
        )

        return JobDiscoveryService.process_jobs(
            db=db,
            jobs=discovered_jobs
        )