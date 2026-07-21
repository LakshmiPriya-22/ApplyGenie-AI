from sqlalchemy.orm import Session

from app.models.resume_analysis import ResumeAnalysis


class ResumeAnalysisRepository:

    @staticmethod
    def create(
        db: Session,
        resume_id: int,
        analysis: dict
    ):

        resume_analysis = ResumeAnalysis(
            resume_id=resume_id,
            analysis=analysis,
            status="COMPLETED"
        )

        db.add(resume_analysis)
        db.commit()
        db.refresh(resume_analysis)

        return resume_analysis

    @staticmethod
    def get_by_resume_id(
        db: Session,
        resume_id: int
    ):

        return (
            db.query(ResumeAnalysis)
            .filter(
                ResumeAnalysis.resume_id == resume_id
            )
            .first()
        )

    @staticmethod
    def delete(
        db: Session,
        analysis: ResumeAnalysis
    ):
        db.delete(analysis)
        db.commit()