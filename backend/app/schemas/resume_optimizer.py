from pydantic import BaseModel


class ResumeOptimizerRequest(BaseModel):
    resume_id: int
    job_description: str


class ResumeOptimizerResponse(BaseModel):
    optimized_resume: str