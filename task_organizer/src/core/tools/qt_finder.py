from abc import ABC
from typing import Type, Optional
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget, QLineEdit, QListWidget, \
    QCalendarWidget, QTimeEdit, QToolButton, QComboBox


class QtFinder(ABC):
    @staticmethod
    def find_widget(window: QWidget, widget: Type, name: str) -> Optional[QObject]:
        return window.findChild(widget, name)

    def __init__(self, window: QWidget):
        super().__init__()
        self.window = window

    def find_line_edit(self, name: str) -> Optional[QLineEdit]:
        return QtFinder.find_widget(self.window, QLineEdit, name)

    def find_calendar_widget(self, name: str) -> Optional[QCalendarWidget]:
        return QtFinder.find_widget(self.window, QCalendarWidget, name)

    def find_time_edit(self, name: str) -> Optional[QTimeEdit]:
        return QtFinder.find_widget(self.window, QTimeEdit, name)

    def find_button(self, name: str) -> Optional[QToolButton]:
        return QtFinder.find_widget(self.window, QToolButton, name)

    def find_list_widget(self, name: str) -> Optional[QListWidget]:
        return QtFinder.find_widget(self.window, QListWidget, name)

    def find_combo_box(self, name: str) -> Optional[QComboBox]:
        return QtFinder.find_widget(self.window, QComboBox, name)
