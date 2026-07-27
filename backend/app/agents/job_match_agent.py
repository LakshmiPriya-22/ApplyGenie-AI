from sqlalchemy.orm import Session

from app.repositories.resume_repository import ResumeRepository
from app.repositories.job_repository import JobRepository
from app.services.job_match_service import JobMatchService


class JobMatchAgent:
    """
    Matches every resume with every discovered job.
    """

    @staticmethod
    def generate_matches(
        db: Session
    ):

        resumes = ResumeRepository.get_all(db)
        jobs = JobRepository.get_all(db)

        total_resumes = len(resumes)
        total_jobs = len(jobs)

        matches_created = 0
        failed_matches = 0

        for resume in resumes:

            for job in jobs:

                try:

                    JobMatchService.match_resume(
                        db=db,
                        user_id=resume.user_id,
                        resume_id=resume.id,
                        job_id=job.id
                    )

                    matches_created += 1

                except Exception as e:

                    print(
                        f"Resume {resume.id} | Job {job.id} -> {e}"
                    )

                    failed_matches += 1

        return {
            "total_resumes": total_resumes,
            "total_jobs": total_jobs,
            "matches_created": matches_created,
            "failed_matches": failed_matches
        }