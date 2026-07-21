from sqlalchemy.orm import Session

from app.models.interview import Interview


class InterviewRepository:

    @staticmethod
    def create_interview(
        db: Session,
        user_id: int,
        resume_id: int,
        job_id: int,
        job_match_id: int,
        interview_type: str,
        difficulty: str,
        questions: list
    ):

        interview = Interview(
            user_id=user_id,
            resume_id=resume_id,
            job_id=job_id,
            job_match_id=job_match_id,
            interview_type=interview_type,
            difficulty=difficulty,
            questions=questions
        )

        db.add(interview)
        db.commit()
        db.refresh(interview)

        return interview

    @staticmethod
    def get_interview_by_id(
        db: Session,
        interview_id: int
    ):

        return (
            db.query(Interview)
            .filter(Interview.id == interview_id)
            .first()
        )

    @staticmethod
    def get_user_interviews(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Interview)
            .filter(Interview.user_id == user_id)
            .order_by(Interview.created_at.desc())
            .all()
        )

    @staticmethod
    def interview_exists(
        db: Session,
        resume_id: int,
        job_id: int,
        interview_type: str,
        difficulty: str
    ):

        return (
            db.query(Interview)
            .filter(
                Interview.resume_id == resume_id,
                Interview.job_id == job_id,
                Interview.interview_type == interview_type,
                Interview.difficulty == difficulty
            )
            .first()
        )

    @staticmethod
    def update_answers(
        db: Session,
        interview: Interview,
        answers: list
    ):

        interview.answers = answers

        db.commit()
        db.refresh(interview)

        return interview

    @staticmethod
    def update_feedback(
        db: Session,
        interview: Interview,
        feedback: dict,
        score: float
    ):

        interview.feedback = feedback
        interview.score = score

        db.commit()
        db.refresh(interview)

        return interview

    @staticmethod
    def delete_interview(
        db: Session,
        interview: Interview
    ):

        db.delete(interview)
        db.commit()

    @staticmethod
    def get_job_interviews(
        db: Session,
        job_id: int
    ):

        return (
            db.query(Interview)
            .filter(Interview.job_id == job_id)
            .order_by(Interview.created_at.desc())
            .all()
        )

    @staticmethod
    def get_resume_interviews(
        db: Session,
        resume_id: int
    ):

        return (
            db.query(Interview)
            .filter(Interview.resume_id == resume_id)
            .order_by(Interview.created_at.desc())
            .all()
        )

    @staticmethod
    def get_completed_interviews(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Interview)
            .filter(
                Interview.user_id == user_id,
                Interview.feedback.isnot(None)
            )
            .order_by(Interview.created_at.desc())
            .all()
        )