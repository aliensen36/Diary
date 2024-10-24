class Event:
    def __init__(self, title, description, time, date):
        self.title = title
        self.description = description
        self.time = time
        self.date = date

    def __str__(self):
        return f"Event: {self.title}\nDate: {self.date}\nTime: {self.time}\nDescription: {self.description}"

class Diary:
    def __init__(self):
        self.events = []  # Хранит события

    def view_events(self, date):
        # Возвращает события для заданной даты
        return [event for event in self.events if event.date == date]

    def add_event(self, event):
        self.events.append(event)
