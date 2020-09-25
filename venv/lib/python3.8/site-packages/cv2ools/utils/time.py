import time

import torch
from loguru import logger


class Average(object):

    def __init__(self):
        self.sum = 0
        self.count = 0

    def update(self, value):
        self.sum += value
        self.count += 1

    @property
    def value(self):
        if self.count == 0:
            return float('inf')
        else:
            return self.sum / self.count


def sync_perf_counter():
    if torch.cuda.is_available():
        torch.cuda.synchronize()

    return time.perf_counter()


def timeit(func):
    average = Average()

    def timed(*args, **kwargs):
        start = sync_perf_counter()
        output = func(*args, **kwargs)
        t = sync_perf_counter() - start

        average.update(t)

        logger.debug('%s took %.6f seconds, average: %.6f seconds, fps: %.2f', func.__qualname__, t, average.value,
                     1 / average.value)
        return output

    return timed
