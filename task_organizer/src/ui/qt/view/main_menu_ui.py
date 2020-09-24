from PyQt5 import uic
from PyQt5.QtCore import QDateTime, QTime
from src.ui.qt.view.qt_view import QtView


class MainMenuUi(QtView):
    form, window = uic.loadUiType("ui/qt/form/task_organizer.ui")

    def __init__(self):
        super().__init__(MainMenuUi.window())
        self.form = MainMenuUi.form()
        self.form.setupUi(self.window)
        self.lineEdit = self.qt.find_line_edit('lineEdit')
        self.dateBox = self.qt.find_calendar_widget('calendarWidget')
        self.timeEdit = self.qt.find_time_edit('timeEdit')
        self.buttonBox = self.qt.find_button_box('buttonBox')
        self.taskList = self.qt.find_list_widget('taskList')
        self.today_date = None
        self.taskItems = []
        self.setup_ui()

    def setup_ui(self):
        self.calendar_settings()
        self.time_settings()
        self.buttonBox.clicked.connect(self.button_box_clicked)

    def show(self):
        self.window.show()

    def calendar_settings(self):
        self.dateBox.showToday()
        self.today_date = self.dateBox.selectedDate()
        self.dateBox.setMinimumDate(self.today_date)

    def time_settings(self):
        time_now = QTime.currentTime()
        self.timeEdit.setTime(time_now)

    def button_box_clicked(self):
        for button in self.buttonBox.buttons():
            if button.text() == 'Reset':
                self.dateBox.setSelectedDate(self.today_date)
                self.time_settings()
                self.lineEdit.setText('')
                self.window.repaint()
            elif button.text() == 'Save':
                date_time = self.dateBox.dateTime().strftime('%Y, %m, %d')
                self.taskItems.append(f'{self.lineEdit.text()} - {date_time}')
                print(self.taskItems)
