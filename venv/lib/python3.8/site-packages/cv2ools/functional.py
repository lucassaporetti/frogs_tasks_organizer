import os
import urllib
from typing import Iterable

import cv2
import numpy as np
from loguru import logger

from .core import Displayer, VideoFileStream, VideoStream, VideoWriter


def _is_url(s: str) -> bool:
    try:
        result = urllib.parse.urlparse(s)
        return all([result.scheme, result.netloc, result.path])
    except Exception as e:
        logger.debug(e)
        return False


def _is_file(s):
    return os.path.exists(s)


def read_video(filename):
    stream = VideoStream(filename)
    for img in stream:
        yield img


def display_video(src, fps=None):
    logger.debug('the type of {} is {}', src, type(src))
    if isinstance(src, int):
        stream = VideoStream(src)
    elif _is_file(src):
        stream = VideoFileStream(src)
    elif _is_url(src):
        stream = VideoStream(src)
    else:
        raise ValueError('filename is invalid')

    if fps is not None:
        stream.fps = fps

    displayer = Displayer(stream)
    displayer.display()


def write_video(images: Iterable[np.ndarray], filename: str, fps: float, **kwargs):
    r"""Convert images to a video"""
    with VideoWriter(filename, fps, **kwargs) as writer:
        for image in images:
            writer.write(image)


def read_images(paths):
    for path in paths:
        img = cv2.imread(path)
        if img is not None:
            yield img
        else:
            continue
