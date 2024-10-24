from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel, QSizePolicy, QListWidgetItem


class DiaryApp(QWidget):
    def __init__(self, diary):
        super().__init__()
        self.diary = diary
        self.selected_date = datetime.today()  # Пример текущей даты

        # Создаем макет
        layout = QVBoxLayout()

        self.events_list = QListWidget()  # Используем QListWidget
        layout.addWidget(self.events_list)  # Добавляем список в макет
        self.setLayout(layout)

        self.update_events_list()

    def update_events_list(self):
        self.events_list.clear()  # Очищаем список

        events = self.diary.view_events(datetime.combine(self.selected_date, datetime.min.time()))

        if events:
            for event in events:
                # Создаем QLabel для отображения события
                label = QLabel(f"{event.time.strftime('%H:%M')} - {event.title} ({event.description})")
                label.setWordWrap(True)  # Включаем перенос слов
                label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)  # Настраиваем политику размера
                label.setContentsMargins(5, 5, 5, 5)  # Отступы

                # Создаем QListWidgetItem и добавляем QLabel в него
                item = QListWidgetItem(self.events_list)
                item.setSizeHint(label.sizeHint())  # Устанавливаем размер элемента в зависимости от QLabel

                # Добавляем элемент в список
                self.events_list.addItem(item)  # Добавляем элемент в список
                self.events_list.setItemWidget(item, label)  # Устанавливаем QLabel как виджет для элемента

        else:
            self.events_list.addItem("Нет событий на этот день")  # Добавляем сообщение, если нет событий
