import json

from groq import Groq

from app.config.settings import settings
from app.core.logger import logger

client = Groq(
    api_key=settings.GROQ_API_KEY
)


class AIInterviewService:

    @staticmethod
    def generate_interview(
        resume_analysis: dict,
        job,
        match,
        interview_type: str,
        difficulty: str
    ):

        logger.info("Generating AI interview questions...")

        prompt = f"""
You are a Senior Technical Interviewer.

Generate interview questions based on:

Resume Analysis:
{json.dumps(resume_analysis, indent=2)}

Job Details:

Title:
{job.title}

Company:
{job.company}

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

Return ONLY valid JSON.

Example:

[
    {{
        "question":"Explain Dependency Injection in FastAPI.",
        "category":"Technical"
    }},
    {{
        "question":"Tell me about yourself.",
        "category":"HR"
    }}
]

Rules:

Generate exactly 10 questions.

If interview_type is:

Technical
→ Technical questions only.

HR
→ HR questions only.

Behavioral
→ Behavioral questions only.

Coding
→ Coding questions only.

Mixed
→ Mix all categories.

Do NOT return markdown.
Do NOT explain anything.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        result = response.choices[0].message.content

        logger.info("Interview generated successfully.")

        return json.loads(result)

    @staticmethod
    def evaluate_answers(
        questions,
        answers
    ):

        logger.info("Evaluating interview answers...")

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

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        result = response.choices[0].message.content

        logger.info("Interview evaluation completed.")

        return json.loads(result)