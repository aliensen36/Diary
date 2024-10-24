class Diary:
    def __init__(self):
        self.events = []  # Хранит события

    def view_events(self, date):
        # Возвращает события для заданной даты
        return [event for event in self.events if event.date == date]

    def add_event(self, event):
        self.events.append(event)
