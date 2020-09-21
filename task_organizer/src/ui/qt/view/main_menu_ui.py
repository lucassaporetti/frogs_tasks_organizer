from PyQt5 import uic
from PyQt5.QtCore import QDateTime

from src.ui.qt.view.qt_view import QtView


class MainMenuUi(QtView):
    form, window = uic.loadUiType("ui/qt/form/task_organizer.ui")

    def __init__(self):
        super().__init__(MainMenuUi.window())
        self.form = MainMenuUi.form()
        self.form.setupUi(self.window)
        self.lineEdit = self.qt.find_line_edit('lineEdit')
        self.dateBox = self.qt.find_date_time_edit('dateBox')
        self.buttonBox = self.qt.find_button_box('buttonBox')
        self.taskList = self.qt.find_list_widget('taskList')
        self.taskItems = []
        self.setup_ui()

    def setup_ui(self):
        self.buttonBox.clicked.connect(self.button_box_clicked)

    def show(self):
        self.window.show()

    def button_box_clicked(self):
        for button in self.buttonBox.buttons():
            if button.text() == 'Reset':
                date_time = QDateTime(2020, 1, 1, 00, 00)
                self.lineEdit.setText('')
                self.dateBox.setDateTime(date_time)
                self.window.repaint()
            elif button.text() == 'Save':
                date_time = self.dateBox.dateTime().strftime('%Y, %m, %d')
                self.taskItems.append(f'{self.lineEdit.text()} - {date_time}')
                print(self.taskItems)
