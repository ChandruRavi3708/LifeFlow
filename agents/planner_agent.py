from utils.logger import logger
from google import genai

class PlannerAgent:
    def __init__(self, memory):
        self.memory = memory
        self.client = genai.Client()

    def plan_day(self, tasks, preferences):
        logger.info("PlannerAgent: Creating daily plan...")

        prompt = f"""
        Create a structured day plan.
        Tasks: {tasks}
        Preferences: {preferences}
        Format as bullet list.
        """

        response = self.client.models.generate_text(
            model="gemini-2.0-flash",
            prompt=prompt
        )

        plan = response.text
        self.memory.write("last_plan", plan)
        return plan
