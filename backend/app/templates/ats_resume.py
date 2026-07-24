from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)


class ATSResumeTemplate:

    def __init__(self, output_path: str):

        self.doc = SimpleDocTemplate(
            output_path,
            rightMargin=0.6 * inch,
            leftMargin=0.6 * inch,
            topMargin=0.6 * inch,
            bottomMargin=0.6 * inch
        )

        self.styles = getSampleStyleSheet()

        # -----------------------------
        # Name Style
        # -----------------------------
        self.styles["Title"].fontName = "Helvetica-Bold"
        self.styles["Title"].fontSize = 22
        self.styles["Title"].alignment = TA_CENTER
        self.styles["Title"].spaceAfter = 6

        # -----------------------------
        # Heading Style
        # -----------------------------
        self.styles["Heading2"].fontName = "Helvetica-Bold"
        self.styles["Heading2"].fontSize = 13
        self.styles["Heading2"].textColor = colors.darkblue
        self.styles["Heading2"].spaceBefore = 12
        self.styles["Heading2"].spaceAfter = 6

        # -----------------------------
        # Body Style
        # -----------------------------
        self.styles["BodyText"].fontName = "Helvetica"
        self.styles["BodyText"].fontSize = 10
        self.styles["BodyText"].leading = 16

        self.story = []

    # ==========================================
    # Helper Methods
    # ==========================================

    def add_title(self, title: str):

        self.story.append(
            Paragraph(title, self.styles["Title"])
        )

    def add_heading(self, heading: str):

        self.story.append(
            Paragraph(heading, self.styles["Heading2"])
        )

    def add_paragraph(self, text: str):

        self.story.append(
            Paragraph(text, self.styles["BodyText"])
        )

        self.story.append(
            Spacer(1, 6)
        )

    def add_bullets(self, items):

        for item in items:

            self.story.append(
                Paragraph(
                    f"• {item}",
                    self.styles["BodyText"]
                )
            )

        self.story.append(
            Spacer(1, 8)
        )

    def add_horizontal_line(self):

        table = Table([[""]], colWidths=[7.2 * inch])

        table.setStyle(
            TableStyle([
                ("LINEBELOW", (0, 0), (-1, -1), 1, colors.grey)
            ])
        )

        self.story.append(table)

        self.story.append(
            Spacer(1, 10)
        )

    # ==========================================
    # Header
    # ==========================================

    def add_header(self, data: dict):

        name = data.get("name", "").strip()

        if not name:
            name = "ATS Optimized Resume"

        self.add_title(name)

        contact = []

        if data.get("email"):
            contact.append(data["email"])

        if data.get("phone"):
            contact.append(data["phone"])

        if data.get("linkedin"):
            contact.append(data["linkedin"])

        if data.get("github"):
            contact.append(data["github"])

        if contact:
            self.story.append(
                Paragraph(
                    " | ".join(contact),
                    self.styles["BodyText"]
                )
            )

        self.story.append(Spacer(1, 10))

        self.add_horizontal_line()

    # ==========================================
    # Professional Summary
    # ==========================================

    def add_summary(self, data: dict):

        summary = data.get("summary", "").strip()

        if not summary:
            return

        self.add_heading("Professional Summary")

        self.add_paragraph(summary)

        self.add_horizontal_line()

    # ==========================================
    # Technical Skills
    # ==========================================

    def add_skills(self, data: dict):

        skills = data.get("skills", [])

        if not skills:
            return

        self.add_heading("Technical Skills")

        rows = []

        row = []

        for skill in skills:

            row.append(f"• {skill}")

            if len(row) == 2:
                rows.append(row)
                row = []

        if row:
            while len(row) < 2:
                row.append("")
            rows.append(row)

        table = Table(rows, colWidths=[3.3 * inch, 3.3 * inch])

        table.setStyle(
            TableStyle([
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("VALIGN", (0, 0), (-1, -1), "TOP")
            ])
        )

        self.story.append(table)

        self.story.append(Spacer(1, 10))

        self.add_horizontal_line()

    # ==========================================
    # Projects
    # ==========================================

    def add_projects(self, data: dict):

        projects = data.get("projects", [])

        if not projects:
            return

        self.add_heading("Projects")

        for project in projects:

            title = project.get("title", "").strip()
            description = project.get("description", "").strip()
            technologies = project.get("technologies", "").strip()

            # Project Title
            if title:
                self.story.append(
                    Paragraph(
                        f"<b>{title}</b>",
                        self.styles["BodyText"]
                    )
                )

            # Project Description
            if description:

                points = [
                    p.strip()
                    for p in description.split(".")
                    if p.strip()
                ]

                if points:

                    for point in points:

                        self.story.append(
                            Paragraph(
                                f"• {point}",
                                self.styles["BodyText"]
                            )
                        )

                else:

                    self.story.append(
                        Paragraph(
                            description,
                            self.styles["BodyText"]
                        )
                    )

            # Technologies Used
            if technologies:

                self.story.append(
                    Paragraph(
                        f"<b>Technologies:</b> {technologies}",
                        self.styles["BodyText"]
                    )
                )

            self.story.append(
                Spacer(1, 12)
            )

        self.add_horizontal_line()

    # ==========================================
    # ATS Score
    # ==========================================

    def add_ats_score(self, data: dict):

        score = data.get("ats_score", "")

        if not score:
            return

        self.add_heading("ATS Match Score")

        table = Table(
            [[f"{score} / 100"]],
            colWidths=[2 * inch]
        )

        table.setStyle(
            TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), colors.lightgrey),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.darkblue),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 16),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("GRID", (0, 0), (-1, -1), 1, colors.grey)
            ])
        )

        self.story.append(table)

        self.story.append(
            Spacer(1, 12)
        )

        self.add_horizontal_line()

        # ==========================================
    # Education
    # ==========================================

    def add_education(self, data: dict):

        education = data.get("education", "").strip()

        if not education:
            return

        self.add_heading("Education")
        self.add_paragraph(education)
        self.add_horizontal_line()

    # ==========================================
    # Certifications
    # ==========================================

    def add_certifications(self, data: dict):

        certifications = data.get("certifications", [])

        if not certifications:
            return

        self.add_heading("Certifications")
        self.add_bullets(certifications)
        self.add_horizontal_line()

    # ==========================================
    # Achievements
    # ==========================================

    def add_achievements(self, data: dict):

        achievements = data.get("achievements", [])

        if not achievements:
            return

        self.add_heading("Achievements")
        self.add_bullets(achievements)
        self.add_horizontal_line()

    # ==========================================
    # Missing Skills
    # ==========================================

    def add_missing_skills(self, data: dict):

        skills = data.get("missing_skills", [])

        if not skills:
            return

        self.add_heading("Recommended Skills to Learn")
        self.add_bullets(skills)
        self.add_horizontal_line()

    # ==========================================
    # Improvement Suggestions
    # ==========================================

    def add_suggestions(self, data: dict):

        suggestions = data.get("suggestions", [])

        if not suggestions:
            return

        self.add_heading("Resume Improvement Suggestions")
        self.add_bullets(suggestions)

    # ==========================================
    # Build Resume
    # ==========================================

    def build(self, data: dict):

        self.add_header(data)

        self.add_summary(data)

        self.add_skills(data)

        self.add_projects(data)

        self.add_education(data)

        self.add_certifications(data)

        self.add_achievements(data)

        self.add_ats_score(data)

        self.add_missing_skills(data)

        self.add_suggestions(data)

        self.doc.build(self.story)