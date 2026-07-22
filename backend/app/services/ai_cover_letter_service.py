import json

from groq import Groq

from app.config.settings import settings
from app.core.logger import logger

client = Groq(
    api_key=settings.GROQ_API_KEY
)


class AICoverLetterService:

    @staticmethod
    def generate_cover_letter(
        resume_analysis: dict,
        job,
        match
    ):

        logger.info("Generating AI cover letter...")

        prompt = f"""
You are an expert career coach and professional resume writer.

Generate a personalized, professional, ATS-friendly cover letter.

Candidate Resume Analysis:
{json.dumps(resume_analysis, indent=2)}

Job Details:

Title:
{job.title}

Company:
{job.company}

Location:
{job.location}

Description:
{job.description}

Requirements:
{job.requirements}

Skills:
{job.skills}

Resume Match Score:
{match.match_score}

Candidate Strengths:
{match.strengths}

Missing Skills:
{match.missing_skills}

Recommendations:
{match.recommendations}

Instructions:

1. Address the hiring manager professionally.
2. Mention the job title and company.
3. Highlight the candidate's relevant skills.
4. Mention how the candidate's experience aligns with the role.
5. Keep a confident and professional tone.
6. Keep the length between 300–500 words.
7. Do not mention the match score.
8. Do not mention missing skills.
9. End with a professional closing.

Return ONLY the cover letter text.
Do NOT use markdown.
Do NOT wrap the response in JSON.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4
        )

        cover_letter = response.choices[0].message.content.strip()

        logger.info("Cover letter generated successfully.")

        return cover_letter