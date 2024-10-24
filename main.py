import sys
from PyQt5.QtWidgets import QApplication
from ui import DiaryApp
from diary import Diary

if __name__ == '__main__':
    app = QApplication(sys.argv)
    diary = Diary()
    window = DiaryApp(diary)
    window.show()
    sys.exit(app.exec_())
