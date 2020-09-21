from abc import ABC
from typing import Type, Optional
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget, QLineEdit, QDialogButtonBox, QListWidget, QDateTimeEdit


class QtFinder(ABC):
    @staticmethod
    def find_widget(window: QWidget, widget: Type, name: str) -> Optional[QObject]:
        return window.findChild(widget, name)

    def __init__(self, window: QWidget):
        super().__init__()
        self.window = window

    def find_line_edit(self, name: str) -> Optional[QLineEdit]:
        return QtFinder.find_widget(self.window, QLineEdit, name)

    def find_date_time_edit(self, name: str) -> Optional[QDateTimeEdit]:
        return QtFinder.find_widget(self.window, QDateTimeEdit, name)

    def find_button_box(self, name: str) -> Optional[QDialogButtonBox]:
        return QtFinder.find_widget(self.window, QDialogButtonBox, name)

    def find_list_widget(self, name: str) -> Optional[QListWidget]:
        return QtFinder.find_widget(self.window, QListWidget, name)
