from pydantic import BaseModel


class ResumePDFRequest(BaseModel):
    resume_id: int
    job_description: str