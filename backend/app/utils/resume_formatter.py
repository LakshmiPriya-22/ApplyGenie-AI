import re


class ResumeFormatter:

    @staticmethod
    def clean_line(line: str) -> str:
        """Remove markdown formatting."""

        line = line.strip()

        # Remove markdown headings
        line = re.sub(r"^#{1,6}\s*", "", line)

        # Remove bold/italic
        line = line.replace("**", "")
        line = line.replace("__", "")
        line = line.replace("*", "")

        # Remove code fences
        line = line.replace("```markdown", "")
        line = line.replace("```", "")

        # Convert markdown links
        line = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", line)

        # Normalize spaces
        line = re.sub(r"\s+", " ", line)

        return line.strip()

    @staticmethod
    def format(ai_response: str):

        data = {
            "name": "",
            "email": "",
            "phone": "",
            "linkedin": "",
            "github": "",
            "summary": "",
            "skills": [],
            "projects": [],
            "education": "",
            "certifications": [],
            "achievements": [],
            "ats_score": "",
            "missing_skills": [],
            "suggestions": []
        }

        current_section = None
        current_project = None

        for raw in ai_response.splitlines():

            line = ResumeFormatter.clean_line(raw)

            if not line:
                continue

            lower = line.lower()

            # -----------------------------
            # Skip unwanted headings
            # -----------------------------
            if lower in {
                "optimized soft skills",
                "recommended keywords",
                "final ats-optimized resume",
                "contact information",
                "sources"
            }:
                continue

            # -----------------------------
            # ATS Score
            # -----------------------------
            if "ats match score" in lower or "ats score" in lower:

                score = re.findall(r"\d+", line)

                if score:
                    data["ats_score"] = score[0]

                continue

            # -----------------------------
            # Email
            # -----------------------------
            email = re.search(
                r'[\w\.-]+@[\w\.-]+\.\w+',
                line
            )

            if email and not data["email"]:
                data["email"] = email.group()

            # -----------------------------
            # Phone
            # -----------------------------
            phone = re.search(
                r'(\+?\d[\d\s\-]{8,})',
                line
            )

            if phone and not data["phone"]:
                data["phone"] = phone.group(1)

            # -----------------------------
            # LinkedIn
            # -----------------------------
            if "linkedin" in lower:
                data["linkedin"] = line

            # -----------------------------
            # GitHub
            # -----------------------------
            if "github" in lower:
                data["github"] = line

            # -----------------------------
            # Name
            # -----------------------------
            if (
                not data["name"]
                and len(line.split()) <= 4
                and "resume" not in lower
                and "score" not in lower
                and "skills" not in lower
            ):
                if re.match(r"^[A-Za-z .]+$", line):
                    data["name"] = line

            # -----------------------------
            # Sections
            # -----------------------------
            if "professional summary" in lower:
                current_section = "summary"
                continue

            if "technical skills" in lower:
                current_section = "skills"
                continue

            if "projects" == lower or "project" == lower:
                current_section = "projects"
                continue

            if "education" in lower:
                current_section = "education"
                continue

            if "certifications" in lower:
                current_section = "certifications"
                continue

            if "achievements" in lower:
                current_section = "achievements"
                continue

            if "missing skills" in lower:
                current_section = "missing_skills"
                continue

            if (
                "resume improvement suggestions" in lower
                or "improvement suggestions" in lower
            ):
                current_section = "suggestions"
                continue

            # -----------------------------
            # Summary
            # -----------------------------
            if current_section == "summary":

                data["summary"] += line + " "

            # -----------------------------
            # Skills
            # -----------------------------
            elif current_section == "skills":

                skill = line.lstrip("•-+ ").strip()

                if (
                    skill
                    and len(skill) < 80
                    and skill not in data["skills"]
                ):
                    data["skills"].append(skill)

            # -----------------------------
            # Projects
            # -----------------------------
            elif current_section == "projects":

                if line.startswith(("•", "-", "+")):

                    if current_project:
                        current_project["description"] += (
                            line.lstrip("•-+ ").strip()
                            + " "
                        )

                else:

                    if current_project:
                        data["projects"].append(current_project)

                    current_project = {
                        "title": line,
                        "description": "",
                        "technologies": ""
                    }

            # -----------------------------
            # Education
            # -----------------------------
            elif current_section == "education":

                data["education"] += line + " "

            # -----------------------------
            # Certifications
            # -----------------------------
            elif current_section == "certifications":

                cert = line.lstrip("•-+ ").strip()

                if cert:
                    data["certifications"].append(cert)

            # -----------------------------
            # Achievements
            # -----------------------------
            elif current_section == "achievements":

                item = line.lstrip("•-+ ").strip()

                if item:
                    data["achievements"].append(item)

            # -----------------------------
            # Missing Skills
            # -----------------------------
            elif current_section == "missing_skills":

                item = line.lstrip("•-+ ").strip()

                if item:
                    data["missing_skills"].append(item)

            # -----------------------------
            # Suggestions
            # -----------------------------
            elif current_section == "suggestions":

                item = line.lstrip("•-+ ").strip()

                if item:
                    data["suggestions"].append(item)

        if current_project:
            data["projects"].append(current_project)

        data["summary"] = data["summary"].strip()
        data["education"] = data["education"].strip()

        return data