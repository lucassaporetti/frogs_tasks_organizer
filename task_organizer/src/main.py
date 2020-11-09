#!/usr/bin/env python

"""
  @package: TODO describe
   @script: ${app.py}
  @purpose: ${purpose}
  @created: SEP 19, 2020
   @author: Lucas Saporetti
   @mailto: lucassaporetti@gmail.com
"""

import signal

from src.ui.qt.task_organizer_qt import TaskOrganizerQt
from src.core.config.app_config import AppConfigs


def setup():
    AppConfigs().logger().info(AppConfigs.INSTANCE)


def exit_app(sig=None, frame=None):
    print(frame)
    print('\033[2J\033[H')
    print('Bye.')
    print('')
    exit(sig)


class Main:
    def __init__(self):
        self.configs = AppConfigs.INSTANCE

    def run(self):
        pass


# Application entry point
if __name__ == "__main__":
    signal.signal(signal.SIGINT, exit_app)
    setup()
    TaskOrganizerQt().run()
    exit_app(0)
