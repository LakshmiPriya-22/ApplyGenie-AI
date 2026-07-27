import json

from app.core.logger import logger
from app.rag.rag_service import RAGService
from app.rag.llm import llm


class AIInterviewService:

    @staticmethod
    def generate_interview(
        resume,
        job,
        match,
        interview_type: str,
        difficulty: str
    ):
        """
        Generate interview questions using RAG.
        """

        logger.info("Generating AI interview questions...")

        job_context = f"""
Title: {job.title}

Company: {job.company}

Description:
{job.description}

Requirements:
{job.requirements}

Skills:
{job.skills}

Match Score:
{match.match_score}

Interview Type:
{interview_type}

Difficulty:
{difficulty}
"""

        context = RAGService._get_context(
            user_id=resume.user_id,
            resume_id=resume.id,
            query=job_context
        )

        prompt = f"""
You are a Senior Technical Interviewer.

Resume Context:
{context}

Job Details:
{job_context}

Generate exactly 10 interview questions.

Rules:

- Return ONLY valid JSON.
- Do NOT return markdown.
- Do NOT explain anything.

JSON Format:

[
    {{
        "question": "",
        "category": ""
    }}
]

Interview Type:

Technical -> Technical questions only

HR -> HR questions only

Behavioral -> Behavioral questions only

Coding -> Coding questions only

Mixed -> Mix all categories.
"""

        response = llm.generate(
            prompt=prompt,
            temperature=0.3
        )

        logger.info(
            "Interview generated successfully."
        )

        try:
            return json.loads(response)

        except Exception:

            return [
                {
                    "question": response,
                    "category": "General"
                }
            ]

    @staticmethod
    def evaluate_answers(
        questions,
        answers
    ):

        logger.info(
            "Evaluating interview answers..."
        )

        prompt = f"""
You are an experienced Software Engineering Interviewer.

Interview Questions:

{json.dumps(questions, indent=2)}

Candidate Answers:

{json.dumps(answers, indent=2)}

Evaluate every answer.

Return ONLY valid JSON.

{{
    "score":90,
    "strengths":[
        ""
    ],
    "weaknesses":[
        ""
    ],
    "suggestions":[
        ""
    ],
    "overall_feedback":""
}}

Rules:

Score must be between 0 and 100.

Do NOT return markdown.

Do NOT explain anything.
"""

        response = llm.generate(
            prompt=prompt,
            temperature=0.2
        )

        logger.info(
            "Interview evaluation completed."
        )

        try:
            return json.loads(response)

        except Exception:

            return {
                "score": 0,
                "strengths": [],
                "weaknesses": [],
                "suggestions": [],
                "overall_feedback": response
            }