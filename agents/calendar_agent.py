from utils.logger import logger
from tools.calendar_tool import CalendarTool

class CalendarAgent:
    def __init__(self):
        self.calendar = CalendarTool()

    def schedule(self, event, date):
        logger.info("CalendarAgent: Scheduling event...")
        return self.calendar.schedule_event(event, date)
