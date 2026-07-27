from sqlalchemy.orm import Session

from app.repositories.job_repository import JobRepository


class JobDiscoveryService:

    @staticmethod
    def process_jobs(
        db: Session,
        jobs: list[dict]
    ) -> dict:
        """
        Process discovered jobs.

        Responsibilities:
        - Validate job data
        - Remove duplicates
        - Save new jobs
        - Return statistics
        """

        total_found = len(jobs)
        new_jobs = 0
        duplicates = 0

        for job in jobs:

            title = job.get("title")
            company = job.get("company")

            if not title or not company:
                continue

            existing = JobRepository.get_by_title_company(
                db=db,
                title=title,
                company=company
            )

            if existing:
                duplicates += 1
                continue

            JobRepository.create(
                db=db,
                job_data=job
            )

            new_jobs += 1

        return {
            "total_found": total_found,
            "new_jobs": new_jobs,
            "duplicates": duplicates
        }