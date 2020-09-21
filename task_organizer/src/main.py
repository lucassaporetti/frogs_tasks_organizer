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
from task_organizer.src.ui.qt.task_organizer_qt import TaskOrganizerQt


def exit_app(sig=None, frame=None):
    print(frame)
    print('\033[2J\033[H')
    print('Bye.')
    print('')
    exit(sig)


# Application entry point
if __name__ == "__main__":
    signal.signal(signal.SIGINT, exit_app)
    TaskOrganizerQt().run()
    exit_app(0)
