from utils.logger import logger
from google import genai

class EmailAgent:
    def __init__(self, memory):
        self.memory = memory
        self.client = genai.Client()

    def draft_email(self, purpose, details):
        logger.info("EmailAgent: Drafting email...")

        prompt = f"""
        Write a polite, professional email.
        Purpose: {purpose}
        Details: {details}
        """

        response = self.client.models.generate_text(
            model="gemini-2.0-flash",
            prompt=prompt
        )

        return response.text
