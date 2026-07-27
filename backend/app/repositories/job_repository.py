from sqlalchemy.orm import Session

from app.models.job import Job


class JobRepository:

    @staticmethod
    def get_by_title_company(
        db: Session,
        title: str,
        company: str
    ):

        return (
            db.query(Job)
            .filter(
                Job.title == title,
                Job.company == company
            )
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        job_data: dict
    ):

        job = Job(
            title=job_data["title"],
            company=job_data["company"],
            location=job_data.get("location"),
            employment_type=job_data.get("employment_type"),
            experience_level=job_data.get("experience_level"),
            salary=job_data.get("salary"),
            description=job_data.get("description"),
            requirements=job_data.get("requirements"),
            skills=job_data.get("skills"),
            posted_by=job_data.get("posted_by")
        )

        db.add(job)
        db.commit()
        db.refresh(job)

        return job

    @staticmethod
    def get_all(
        db: Session
    ):

        return (
            db.query(Job)
            .order_by(Job.created_at.desc())
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        job_id: int
    ):

        return (
            db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )

    @staticmethod
    def delete(
        db: Session,
        job: Job
    ):

        db.delete(job)
        db.commit()

    @staticmethod
    def count(
        db: Session
    ):

        return db.query(Job).count()