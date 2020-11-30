import functools
from PyQt5 import uic
from PyQt5.QtCore import QTime, Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QIcon, QPixmap
from core.crud.firebase.firebase_repository import FirebaseRepository
from src.ui.qt.view.qt_view import QtView
from src.core.model.task_model import Task


class MainMenuUi(QtView):
    form, window = uic.loadUiType("ui/qt/form/task_organizer.ui")

    def __init__(self):
        super().__init__(MainMenuUi.window())
        self.new_task = None
        self.selected_item = None
        self.all_data = []
        self.repository = FirebaseRepository()
        self.form = MainMenuUi.form()
        self.form.setupUi(self.window)
        self.lineEdit = self.qt.find_line_edit('lineEdit')
        self.priority_box = self.qt.find_combo_box('priorityBox')
        self.type_box = self.qt.find_combo_box('typeBox')
        self.dateBox = self.qt.find_calendar_widget('calendarWidget')
        self.timeEdit = self.qt.find_time_edit('timeEdit')
        self.buttonSave = self.qt.find_button('save_button')
        self.buttonReset = self.qt.find_button('reset_button')
        self.tasks_table = self.qt.find_table_widget('taskTable')
        self.today_date = None
        self.setup_ui()

    def setup_ui(self):
        self.calendar_settings()
        self.time_settings()
        self.data_load()
        self.priority_box.view().setCursor(Qt.PointingHandCursor)
        self.type_box.view().setCursor(Qt.PointingHandCursor)
        self.buttonSave.clicked.connect(self.button_save_clicked)
        self.buttonReset.clicked.connect(self.button_reset_clicked)
        self.tasks_table.mouseDoubleClickEvent = functools.partial(self.item_click)

    def show(self):
        self.window.show()

    def calendar_settings(self):
        self.dateBox.showToday()
        self.today_date = self.dateBox.selectedDate()
        self.dateBox.setMinimumDate(self.today_date)

    def time_settings(self):
        time_now = QTime.currentTime()
        self.timeEdit.setTime(time_now)

    def data_load(self):
        self.tasks_table.setRowCount(0)
        self.all_data.clear()
        self.all_data = self.repository.get()
        if self.all_data is not None:
            for task in self.all_data:
                if task['priority'] == 'not important / not urgent':
                    selected_priority_icon = QIcon(":/files/green_dot.png")
                elif task['priority'] == 'IMPORTANT / not urgent':
                    selected_priority_icon = QIcon(":/files/blue_dot.png")
                elif task['priority'] == 'not important / URGENT':
                    selected_priority_icon = QIcon(":/files/yellow_dot.png")
                else:
                    selected_priority_icon = QIcon(":/files/red_dot.png")
                status_icon = QIcon(":/files/{}_icon.png".format(task['status'].lower().strip().replace(" ", "")))
                selected_type_icon = QIcon(":/files/{}_icon.png".format(task['task_type'].lower().strip().replace(" ", "")))
                self.tasks_table.insertRow(self.tasks_table.rowCount())
                task_status = QTableWidgetItem()
                task_status.setIcon(status_icon)
                task_status.setText(task['status'])
                task_text = QTableWidgetItem()
                task_text.setText(task['name'])
                task_date = QTableWidgetItem()
                task_date.setText(task['date'])
                task_time = QTableWidgetItem()
                task_time.setText(task['time'])
                task_type = QTableWidgetItem()
                task_type.setIcon(selected_type_icon)
                task_type.setText(task['task_type'])
                task_priority = QTableWidgetItem()
                task_priority.setIcon(selected_priority_icon)
                task_priority.setText(task['priority'])
                task_uuid = QTableWidgetItem()
                task_uuid.setText(task['uuid'])

                self.tasks_table.setItem(self.tasks_table.rowCount() - 1, 0, task_status)
                self.tasks_table.setItem(self.tasks_table.rowCount() - 1, 1, task_text)
                self.tasks_table.setItem(self.tasks_table.rowCount() - 1, 2, task_date)
                self.tasks_table.setItem(self.tasks_table.rowCount() - 1, 3, task_time)
                self.tasks_table.setItem(self.tasks_table.rowCount() - 1, 4, task_type)
                self.tasks_table.setItem(self.tasks_table.rowCount() - 1, 5, task_priority)
                self.tasks_table.setItem(self.tasks_table.rowCount() - 1, 6, task_uuid)
                self.tasks_table.resizeColumnsToContents()

    def button_save_clicked(self):
        selected_date = self.dateBox.selectedDate()
        str_selected_date = selected_date.toString('yyyy/MM/dd')
        selected_time = self.timeEdit.text()
        selected_priority_text = self.priority_box.currentText()
        selected_type_text = self.type_box.currentText()

        self.new_task = self.new_task if self.new_task else Task()
        self.new_task.status = 'To do'
        self.new_task.name = self.lineEdit.text()
        self.new_task.date = str_selected_date
        self.new_task.time = selected_time
        self.new_task.task_type = selected_type_text
        self.new_task.priority = selected_priority_text
        self.repository.insert(self.new_task)

        message = QMessageBox()
        message.setStyleSheet("""
                                                    background-color: rgb(50, 85, 127);
                                                    font: 75 15pt "MS Shell Dlg 2";
                                                    color: rgb(238, 238, 236); 
                                                    """)
        message.setText('Do your jumps, frog!\n\nA new task has been created.')
        message.setWindowTitle('Roll up your sleeves!')
        ok_button = message.addButton('Ok', QMessageBox.ApplyRole)
        ok_button.setCursor(Qt.PointingHandCursor)
        hands_up_icon = QPixmap(":/files/hands_up_icon.png")
        message.setIconPixmap(hands_up_icon)
        message.exec_()

        self.data_load()

        self.button_reset_clicked()

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
        todo_icon = QIcon(":/files/todo_icon.png")
        done_icon = QIcon(":/files/done_icon.png")
        failed_icon = QIcon(":/files/failed_icon.png")
        delete_button = message.addButton('Delete', QMessageBox.ApplyRole)
        failed_status_button = message.addButton('Failed', QMessageBox.ApplyRole)
        todo_status_button = message.addButton('To do', QMessageBox.ApplyRole)
        done_status_button = message.addButton('Done', QMessageBox.ApplyRole)
        delete_button.setCursor(Qt.PointingHandCursor)
        failed_status_button.setCursor(Qt.PointingHandCursor)
        todo_status_button.setCursor(Qt.PointingHandCursor)
        done_status_button.setCursor(Qt.PointingHandCursor)
        failed_status_button.setIcon(failed_icon)
        todo_status_button.setIcon(todo_icon)
        done_status_button.setIcon(done_icon)
        message.exec_()

        selected_row = self.tasks_table.currentRow()
        selected_uuid = self.tasks_table.item(selected_row, 6).text()

        if message.clickedButton() == delete_button:
            self.tasks_table.removeRow(selected_row)
            self.repository.delete(selected_uuid)

        elif message.clickedButton() == failed_status_button:
            self.tasks_table.item(selected_row, 0).setIcon(failed_icon)
            self.tasks_table.item(selected_row, 0).setText('Failed')
        elif message.clickedButton() == todo_status_button:
            self.tasks_table.item(selected_row, 0).setIcon(todo_icon)
            self.tasks_table.item(selected_row, 0).setText('To do')
        elif message.clickedButton() == done_status_button:
            self.tasks_table.item(selected_row, 0).setIcon(done_icon)
            self.tasks_table.item(selected_row, 0).setText('Done')
        self.tasks_table.resizeColumnsToContents()
