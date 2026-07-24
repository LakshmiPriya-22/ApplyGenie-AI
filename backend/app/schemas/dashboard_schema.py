from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_applications: int

    applied: int
    shortlisted: int
    interview_scheduled: int
    interview_completed: int

    offer_received: int
    accepted: int
    rejected: int
    withdrawn: int