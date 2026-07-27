import json
import os

from app.templates.ats_resume import ATSResumeTemplate


class PDFGenerator:

    @staticmethod
    def generate(ai_response):

        # Create output directory
        output_dir = "generated_pdfs"
        os.makedirs(output_dir, exist_ok=True)

        # Output PDF path
        pdf_path = os.path.join(
            output_dir,
            "ATS_Optimized_Resume.pdf"
        )

        # Convert JSON string to dictionary if needed
        if isinstance(ai_response, str):

            ai_response = ai_response.strip()

            # Remove Markdown code fences if present
            if ai_response.startswith("```"):
                ai_response = ai_response.replace("```json", "")
                ai_response = ai_response.replace("```", "")
                ai_response = ai_response.strip()

            data = json.loads(ai_response)

        else:
            data = ai_response

        # Build ATS Resume
        template = ATSResumeTemplate(pdf_path)
        template.build(data)

        return pdf_path
