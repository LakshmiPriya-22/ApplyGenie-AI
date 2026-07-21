import json

from groq import Groq

from app.config.settings import settings
from app.core.logger import logger

client = Groq(
    api_key=settings.GROQ_API_KEY
)


class AIMatchingService:

    @staticmethod
    def match_resume_with_job(
        resume_analysis: dict,
        job
    ):

        logger.info(
            "Generating AI Resume-Job Match..."
        )

        prompt = f"""
You are an expert ATS (Applicant Tracking System) and Technical Recruiter.

Compare the following Resume Analysis with the Job Description.

Return ONLY valid JSON.

Resume Analysis:
{json.dumps(resume_analysis, indent=2)}

Job Details:

Title:
{job.title}

Company:
{job.company}

Location:
{job.location}

Employment Type:
{job.employment_type}

Experience:
{job.experience_level}

Description:
{job.description}

Requirements:
{job.requirements}

Skills:
{job.skills}

Return ONLY this JSON format.

{{
    "match_score": 0,
    "strengths": [],
    "missing_skills": [],
    "recommendations": [],
    "summary": ""
}}

Rules:
- match_score must be between 0 and 100.
- strengths should contain only matching skills.
- missing_skills should contain skills absent in resume.
- recommendations should help improve the resume.
- summary should be less than 60 words.
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

        logger.info(
            "AI Matching completed."
        )

        return json.loads(result)