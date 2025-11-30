from utils.logger import logger
from agents.planner_agent import PlannerAgent
from agents.meal_agent import MealAgent
from agents.email_agent import EmailAgent
from agents.calendar_agent import CalendarAgent

class Orchestrator:
    def __init__(self, session_memory, long_term_memory):
        self.session_memory = session_memory
        self.long_term_memory = long_term_memory

        self.planner = PlannerAgent(session_memory)
        self.meal_agent = MealAgent(session_memory)
        self.email_agent = EmailAgent(session_memory)
        self.calendar_agent = CalendarAgent()

    def run(self, request):
        logger.info("Orchestrator: Processing request...")

        user_pref = self.long_term_memory.read("preferences")

        if "plan my day" in request.lower():
            return self.planner.plan_day(
                tasks=["email clients", "gym", "team meeting"],
                preferences=user_pref
            )

        if "meal" in request.lower():
            diet = user_pref.get("diet", "general")
            return self.meal_agent.meal_plan(diet)

        if "email" in request.lower():
            return self.email_agent.draft_email(
                purpose="Follow-up",
                details="Requesting updates on project status."
            )

        if "schedule" in request.lower():
            return self.calendar_agent.schedule(
                event="Team Sync",
                date="2025-11-20"
            )

        return "LifeFlow didn't understand your request."
