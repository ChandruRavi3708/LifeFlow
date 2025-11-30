class CalendarTool:
    def schedule_event(self, event_name, date):
        return {
            "event": event_name,
            "date": date,
            "status": "scheduled"
        }
