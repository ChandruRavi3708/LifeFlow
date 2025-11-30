from utils.logger import logger
from google import genai

class MealAgent:
    def __init__(self, memory):
        self.memory = memory
        self.client = genai.Client()

    def meal_plan(self, dietary_pref):
        logger.info("MealAgent: Generating meal plan...")

        prompt = f"""
        Create a 3-day meal plan.
        Dietary preference: {dietary_pref}
        Include ingredients for each meal.
        """

        response = self.client.models.generate_text(
            model="gemini-2.0-flash",
            prompt=prompt
        )

        return response.text
