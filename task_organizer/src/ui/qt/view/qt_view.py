from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QWidget
from src.core.config.app_config import *
from logging import log
from src.core.tools.qt_finder import QtFinder


class QtView(ABC):
    def __init__(self, window: QWidget, parent=None):
        super().__init__()
        self.window = window
        self.parent = parent
        self.logger = log
        self.qt = QtFinder(self.window)

    @abstractmethod
    def setup_ui(self):
        pass
