import threading
from queue import Queue

import cv2
import numpy as np
from loguru import logger


class Controller(object):
    pause_key = ord('p')
    quit_key = ord('q')

    def __init__(self):
        self.quit = True

    def control(self, delay):
        key = cv2.waitKey(delay)

        if key == self.pause_key:
            self.wait()
        elif key == self.quit_key:
            self.quit = False

    def wait(self):
        while True:
            key = cv2.waitKey(1)
            if key == self.pause_key:
                break
            elif key == self.quit_key:
                self.quit = False
                break


class Displayer(object):

    def __init__(self, stream, winname=None):
        self.stream = stream
        self.winname = winname or str()

        self._delay = None
        self.controller = Controller()

    def display(self):
        for image in self.stream:
            cv2.imshow(self.winname, image)

            self.controller.control(self.delay)

            if not self.controller.quit:
                self.stream.stop = True
                break

    @property
    def delay(self):
        try:
            if self._delay is None:
                self._delay = int(1000 / self.stream.fps)
            return self._delay
        except AttributeError:
            return 1


class VideoStream(object):

    def __init__(self, filename):
        self.cap = cv2.VideoCapture(filename)

    def __iter__(self):
        return self

    def __next__(self):
        if self.cap.isOpened():
            retval, image = self.cap.read()
            if retval:
                return image

        self.cap.release()
        raise StopIteration


class VideoFileStream(object):

    def __init__(self, filename):
        self.cap = cv2.VideoCapture(filename)
        self.queue = Queue()
        self.thread = threading.Thread(target=self._read)
        self.thread.start()

        self._fps = None
        self.stop = False

    def _read(self):
        while self.cap.isOpened():
            retval, image = self.cap.read()
            if self.stop:
                logger.info('Stop reading stream')
                break
            elif retval:
                self.queue.put(image)
            else:
                break

        self.queue.put(None)
        self.cap.release()

    def __iter__(self):
        return self

    def __next__(self):
        item = self.queue.get()
        if item is None:
            raise StopIteration
        return item

    @property
    def fps(self):
        if self._fps is None:
            self._fps = self.cap.get(cv2.CAP_PROP_FPS)
        return self._fps


class VideoWriter(object):

    def __init__(self, filename: str, fps: float, fourcc: str = 'mp4v'):
        self.filename = filename
        self.fps = fps
        self.fourcc = fourcc

        self.size = None
        self.writer = None
        self._init_done = False

    def write(self, image: np.ndarray):
        if not self._init_done:
            self._init_once(image)
            logger.debug('initialize video writer')

        self.writer.write(image)

    def _init_once(self, image: np.ndarray):
        h, w, _ = image.shape
        self.size = (w, h)
        logger.debug('size of first image: ({}, {})', w, h)
        self.writer = cv2.VideoWriter(filename=self.filename,
                                      apiPreference=cv2.CAP_FFMPEG,
                                      fourcc=cv2.VideoWriter_fourcc(*self.fourcc),
                                      fps=self.fps,
                                      frameSize=self.size)
        self._init_done = True

    def release(self):
        if self.writer is not None:
            self.writer.release()
            logger.debug('release video writer')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.release()

    def __repr__(self):
        format_string = self.__class__.__name__ + '('
        format_string += 'filename={}'.format(self.filename)
        format_string += ', fps={}'.format(self.fps)
        format_string += ', fourcc={}'.format(self.fourcc)
        format_string += ')'
        return format_string
