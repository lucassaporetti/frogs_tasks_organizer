import functools
import io
import cv2
import numpy
import base64
import imageio
from PyQt5 import uic
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QListView, QListWidgetItem, QMessageBox
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
        self.priority_box = self.qt.find_combo_box('priorityBox')
        self.type_box = self.qt.find_combo_box('typeBox')
        self.dateBox = self.qt.find_calendar_widget('calendarWidget')
        self.timeEdit = self.qt.find_time_edit('timeEdit')
        self.buttonSave = self.qt.find_button('save_button')
        self.buttonReset = self.qt.find_button('reset_button')
        self.taskList = self.qt.find_table_widget('taskTable')
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
        self.taskList.mouseDoubleClickEvent = functools.partial(self.item_click)

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
        selected_priority_index = self.priority_box.currentIndex()
        selected_priority_icon = self.priority_box.itemIcon(selected_priority_index)
        selected_priority_text = self.priority_box.currentText()
        selected_type_index = self.type_box.currentIndex()
        selected_type_icon = self.type_box.itemIcon(selected_type_index)
        selected_type_text = self.type_box.currentText()
        self.taskItems.append(f'To do - {self.lineEdit.text()} - {str_selected_date} - {selected_time} - '
                              f'{selected_type_text} - {selected_priority_text}')
        self.taskList.setViewMode(QListView.IconMode)
        list_item = QListWidgetItem()
        item_icon = QIcon()
        item_image = self.str_to_rgb(self.blue_dot)
        height, width, channel = item_image.shape
        bytes_per_line = 3 * width
        q_img = QImage(item_image.data, width, height,
                       bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        item_icon.addPixmap(QPixmap(q_img),
                            QIcon.Normal, QIcon.Off)
        # list_item.setIcon(item_icon)
        list_item.setIcon(selected_priority_icon)
        list_item.setIcon(selected_type_icon)
        list_item.setText(f'{self.lineEdit.text()} - {str_selected_date} - {selected_time} - {selected_type_text}'
                          f' - {selected_priority_text}')
        message = QMessageBox()
        message.setStyleSheet("""
                                            background-color: rgb(50, 85, 127);
                                            font: 75 13pt "MS Shell Dlg 2";
                                            color: rgb(238, 238, 236); 
                                            """)
        message.setText('A new task has been created.')
        message.setWindowTitle('Roll up your sleeves!')
        message.setStandardButtons(QMessageBox.Ok)
        message.exec_()
        self.taskList.addItem(list_item)
        self.button_reset_clicked()
        print(self.taskItems)

    def button_reset_clicked(self):
        self.priority_box.setCurrentIndex(-1)
        self.type_box.setCurrentIndex(-1)
        self.dateBox.setSelectedDate(self.today_date)
        self.time_settings()
        self.lineEdit.setText('')
        self.window.repaint()

    def item_click(self, event):
        message = QMessageBox()
        message.setStyleSheet("""
                                                    background-color: rgb(50, 85, 127);
                                                    font: 75 13pt "MS Shell Dlg 2";
                                                    color: rgb(238, 238, 236); 
                                                    """)
        message.setText('Choose the new status:')
        message.setWindowTitle('Change Status')
        blue_icon = QIcon()
        green_icon = QIcon()
        red_icon = QIcon()
        blue_button_image = self.str_to_rgb(self.blue_dot)
        height, width, channel = blue_button_image.shape
        bytes_per_line = 3 * width
        q_img = QImage(blue_button_image.data, width, height,
                       bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        blue_icon.addPixmap(QPixmap(q_img))
        green_button_image = self.str_to_rgb(self.green_dot)
        height, width, channel = green_button_image.shape
        bytes_per_line = 3 * width
        q_img = QImage(green_button_image.data, width, height,
                       bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        green_icon.addPixmap(QPixmap(q_img))
        red_button_image = self.str_to_rgb(self.red_dot)
        height, width, channel = red_button_image.shape
        bytes_per_line = 3 * width
        q_img = QImage(red_button_image.data, width, height,
                       bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        red_icon.addPixmap(QPixmap(q_img))
        delete_button = message.addButton('Delete', QMessageBox.ActionRole)
        red_status_button = message.addButton('Failed', QMessageBox.ActionRole)
        blue_status_button = message.addButton('Doing', QMessageBox.ActionRole)
        green_status_button = message.addButton('Done', QMessageBox.ActionRole)
        red_status_button.setIcon(red_icon)
        blue_status_button.setIcon(blue_icon)
        green_status_button.setIcon(green_icon)
        message.exec_()
        if message.clickedButton() == delete_button:
            selected_item = self.taskList.currentRow()
            self.taskList.takeItem(selected_item)
        elif message.clickedButton() == red_status_button:
            self.taskList.currentItem().setIcon(red_icon)
        elif message.clickedButton() == blue_status_button:
            self.taskList.currentItem().setIcon(blue_icon)
        elif message.clickedButton() == green_status_button:
            self.taskList.currentItem().setIcon(green_icon)

    @staticmethod
    def str_to_rgb(base64_str):
        image_data = base64.b64decode(base64_str)
        image = imageio.imread(io.BytesIO(image_data))
        return cv2.cvtColor(numpy.array(image), cv2.COLOR_BGR2RGB)
