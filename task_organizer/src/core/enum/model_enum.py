from enum import Enum


class Model(Enum):
    TASK = 1

    def __str__(self):
        return "{}".format(self.name.upper())
