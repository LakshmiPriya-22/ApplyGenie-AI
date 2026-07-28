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

        context, _ = RAGService._get_context(
            user_id=resume.user_id,
            resume_id=resume.id,
            query=job_context
        )

        prompt = f"""
You are a Senior Software Engineering Interviewer.

Resume Context:

{context}

Job Details:

{job_context}

Generate an interview preparation plan.

Return ONLY valid JSON.

Do NOT return markdown.
Do NOT explain anything.

Return EXACTLY this format:

{{
    "questions":[
        {{
            "question":"",
            "category":"",
            "difficulty":""
        }}
    ],

    "tips":[
        ""
    ],

    "roadmap":[
        ""
    ],

    "summary":""
}}

Rules:

1. Generate exactly 10 interview questions.
2. Questions must match the resume and job.
3. Include Technical, HR, Behavioural or Coding questions depending on interview_type.
4. Keep difficulty consistent.
5. Give useful interview tips.
6. Give a learning roadmap.
7. Write a short summary.
"""

        response = llm.generate(
            prompt=prompt,
            temperature=0.3
        )

        logger.info("Interview generated successfully.")

        try:
            return json.loads(response)

        except Exception:

            return {
                "questions": [
                    {
                        "question": response,
                        "category": "General",
                        "difficulty": difficulty
                    }
                ],
                "tips": [],
                "roadmap": [],
                "summary": ""
            }

    @staticmethod
    def evaluate_answers(
        questions,
        answers
    ):
        """
        Evaluate candidate interview answers.
        """

        logger.info("Evaluating interview answers...")

        prompt = f"""
You are an experienced Software Engineering interviewer.

Interview Questions:

{json.dumps(questions, indent=2)}

Candidate Answers:

{json.dumps(answers, indent=2)}

Evaluate every answer.

Return ONLY valid JSON.

Return EXACTLY this format:

{{
    "score":90,

    "feedback":[
        {{
            "question":"",
            "rating":9,
            "comment":""
        }}
    ],

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

1. Score between 0 and 100.
2. Rate every answer.
3. Give constructive feedback.
4. Suggest improvements.
5. Return only JSON.
"""

        response = llm.generate(
            prompt=prompt,
            temperature=0.2
        )

        logger.info("Interview evaluation completed.")

        try:
            return json.loads(response)

        except Exception:

            return {
                "score": 0,
                "feedback": [],
                "strengths": [],
                "weaknesses": [],
                "suggestions": [],
                "overall_feedback": response
            }