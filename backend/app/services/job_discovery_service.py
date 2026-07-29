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
        - Remove duplicates within the current discovery run
        - Skip jobs already present in the database
        - Save new jobs
        """

        total_found = len(jobs)
        new_jobs = 0
        duplicates = 0

        # Prevent duplicates returned by providers in the same run
        seen = set()

        for job in jobs:

            title = (job.get("title") or "").strip()
            company = (job.get("company") or "").strip()
            location = (job.get("location") or "").strip()

            if not title or not company:
                continue

            # Case-insensitive duplicate key
            key = (
                title.strip().lower(),
                company.strip().lower(),
                location.strip().lower()
            )

            if key in seen:
                duplicates += 1
                continue

            seen.add(key)

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