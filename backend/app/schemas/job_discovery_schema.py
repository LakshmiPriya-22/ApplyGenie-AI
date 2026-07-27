from pydantic import BaseModel


class JobDiscoveryStatistics(BaseModel):
    total_found: int
    new_jobs: int
    duplicates: int


class JobDiscoveryResponse(BaseModel):
    message: str
    statistics: JobDiscoveryStatistics