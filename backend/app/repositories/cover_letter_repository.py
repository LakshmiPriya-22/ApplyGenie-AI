from sqlalchemy.orm import Session

from app.models.cover_letter import CoverLetter


class CoverLetterRepository:

    @staticmethod
    def create_cover_letter(
        db: Session,
        user_id: int,
        resume_id: int,
        job_id: int,
        job_match_id: int,
        content: str
    ):

        cover_letter = CoverLetter(
            user_id=user_id,
            resume_id=resume_id,
            job_id=job_id,
            job_match_id=job_match_id,
            content=content
        )

        db.add(cover_letter)
        db.commit()
        db.refresh(cover_letter)

        return cover_letter

    @staticmethod
    def get_cover_letter_by_id(
        db: Session,
        cover_letter_id: int
    ):

        return (
            db.query(CoverLetter)
            .filter(CoverLetter.id == cover_letter_id)
            .first()
        )

    @staticmethod
    def get_user_cover_letters(
        db: Session,
        user_id: int
    ):

        return (
            db.query(CoverLetter)
            .filter(CoverLetter.user_id == user_id)
            .order_by(CoverLetter.created_at.desc())
            .all()
        )

    @staticmethod
    def get_cover_letter_by_resume_and_job(
        db: Session,
        resume_id: int,
        job_id: int
    ):

        return (
            db.query(CoverLetter)
            .filter(
                CoverLetter.resume_id == resume_id,
                CoverLetter.job_id == job_id
            )
            .first()
        )

    @staticmethod
    def update_cover_letter(
        db: Session,
        cover_letter: CoverLetter,
        content: str
    ):

        cover_letter.content = content

        db.commit()
        db.refresh(cover_letter)

        return cover_letter

    @staticmethod
    def delete_cover_letter(
        db: Session,
        cover_letter: CoverLetter
    ):

        db.delete(cover_letter)
        db.commit()

    @staticmethod
    def cover_letter_exists(
        db: Session,
        resume_id: int,
        job_id: int
    ):

        return (
            db.query(CoverLetter)
            .filter(
                CoverLetter.resume_id == resume_id,
                CoverLetter.job_id == job_id
            )
            .first()
        )