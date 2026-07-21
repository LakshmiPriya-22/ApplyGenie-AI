from sqlalchemy.orm import Session

from app.models.job_match import JobMatch


class JobMatchRepository:

    @staticmethod
    def create_match(
        db: Session,
        resume_id: int,
        job_id: int,
        match_score: float,
        strengths: list,
        missing_skills: list,
        recommendations: list,
        summary: str,
        ai_response: dict
    ):

        job_match = JobMatch(
            resume_id=resume_id,
            job_id=job_id,
            match_score=match_score,
            strengths=strengths,
            missing_skills=missing_skills,
            recommendations=recommendations,
            summary=summary,
            ai_response=ai_response
        )

        db.add(job_match)
        db.commit()
        db.refresh(job_match)

        return job_match

    @staticmethod
    def get_match(
        db: Session,
        resume_id: int,
        job_id: int
    ):

        return (
            db.query(JobMatch)
            .filter(
                JobMatch.resume_id == resume_id,
                JobMatch.job_id == job_id
            )
            .first()
        )

    @staticmethod
    def get_match_by_id(
        db: Session,
        match_id: int
    ):

        return (
            db.query(JobMatch)
            .filter(JobMatch.id == match_id)
            .first()
        )

    @staticmethod
    def get_matches_by_resume(
        db: Session,
        resume_id: int
    ):

        return (
            db.query(JobMatch)
            .filter(JobMatch.resume_id == resume_id)
            .order_by(JobMatch.created_at.desc())
            .all()
        )

    @staticmethod
    def get_matches_by_job(
        db: Session,
        job_id: int
    ):

        return (
            db.query(JobMatch)
            .filter(JobMatch.job_id == job_id)
            .order_by(JobMatch.created_at.desc())
            .all()
        )

    @staticmethod
    def delete_match(
        db: Session,
        job_match: JobMatch
    ):

        db.delete(job_match)
        db.commit()

    @staticmethod
    def get_all_matches_for_resume(
        db: Session,
        resume_id: int
    ):

        return (
            db.query(JobMatch)
            .filter(JobMatch.resume_id == resume_id)
            .order_by(JobMatch.match_score.desc())
            .all()
        )

    @staticmethod
    def delete_resume_matches(
        db: Session,
        resume_id: int
    ):

        (
            db.query(JobMatch)
            .filter(JobMatch.resume_id == resume_id)
            .delete(synchronize_session=False)
        )

        db.commit()

    @staticmethod
    def get_top_matches_for_resume(
        db: Session,
        resume_id: int,
        limit: int = 10
    ):

        return (
            db.query(JobMatch)
            .filter(JobMatch.resume_id == resume_id)
            .order_by(JobMatch.match_score.desc())
            .limit(limit)
            .all()
        )