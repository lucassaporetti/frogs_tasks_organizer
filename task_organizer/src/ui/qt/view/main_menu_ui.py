import base64

from PyQt5 import uic
from PyQt5.QtCore import QTime
from resources.icons_rgb import DotIcons
from PyQt5.QtGui import QImage, QIcon, QPixmap

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
        self.buttonSave = self.qt.find_button('save_button')
        self.buttonReset = self.qt.find_button('reset_button')
        self.taskList = self.qt.find_list_widget('taskList')
        self.green_dot = DotIcons.green_dot
        self.blue_dot = DotIcons.blue_dot
        self.red_dot = DotIcons.red_dot
        self.today_date = None
        self.taskItems = []
        self.setup_ui()

    def setup_ui(self):
        self.calendar_settings()
        self.time_settings()
        self.buttonSave.clicked.connect(self.button_save_clicked)
        self.buttonReset.clicked.connect(self.button_reset_clicked)

    def show(self):
        self.window.show()

    def calendar_settings(self):
        self.dateBox.showToday()
        self.today_date = self.dateBox.selectedDate()
        self.dateBox.setMinimumDate(self.today_date)

    def time_settings(self):
        time_now = QTime.currentTime()
        self.timeEdit.setTime(time_now)

    def button_save_clicked(self):
        selected_date = self.dateBox.selectedDate()
        str_selected_date = selected_date.toString('yyyy/MM/dd')
        selected_time = self.timeEdit.text()
        self.taskItems.append(f'{self.blue_dot} {self.lineEdit.text()} - {str_selected_date} - {selected_time}')
        self.taskList.addItem(self.taskItems[-1])
        self.button_reset_clicked()
        self.icon_settings()
        print(self.taskItems)

    def button_reset_clicked(self):
        self.dateBox.setSelectedDate(self.today_date)
        self.time_settings()
        self.lineEdit.setText('')
        self.window.repaint()

    def icon_settings(self):
        item_icon = QIcon()
        item_image = base64.b64decode(self.blue_dot)
        image = Image.open(io.BytesIO(bytes))
        height, width, channel = item_image.shape
        bytes_per_line = 3 * width
        q_img = QImage(item_image.data, width, height,
                       bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        item_icon.addPixmap(QPixmap(q_img),
                            QIcon.Normal, QIcon.Off)
        self.taskList.setIcon(item_icon)
