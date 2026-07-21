import re

SKILLS = [
    "Python", "Java", "C", "C++", "SQL", "JavaScript",
    "React", "ReactJS", "HTML", "CSS",
    "FastAPI", "Django", "Flask", "Streamlit",
    "Git", "GitHub", "PostgreSQL",
    "Docker", "AWS", "LangChain", "ChromaDB", "RAG"
]

EDUCATION = [
    "Bachelor",
    "B.Tech",
    "B.E",
    "Master",
    "M.Tech",
    "Intermediate",
    "SSC",
    "CGPA"
]


def analyze_resume(text: str):

    # ---------- Skills ----------
    found_skills = []

    for skill in SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", text, re.IGNORECASE):
            found_skills.append(skill)

    # ---------- Education ----------
    education = []

    for item in EDUCATION:
        if re.search(item, text, re.IGNORECASE):
            education.append(item)

    # ---------- Projects ----------
    project_count = len(
        re.findall(
            r"GitHub|Live Demo",
            text,
            re.IGNORECASE
        )
    )

    # ---------- Certificates ----------
    certificate_count = len(
        re.findall(
            r"Certificate|Badge",
            text,
            re.IGNORECASE
        )
    )

    # ---------- ATS Score ----------
    score = 40

    score += min(len(found_skills) * 3, 30)
    score += min(project_count * 5, 15)
    score += min(certificate_count * 3, 15)

    score = min(score, 100)

    return {
        "skills": found_skills,
        "education": education,
        "projects": project_count,
        "certificates": certificate_count,
        "ats_score": score
    }