import uuid
from src.core.model.entity import Entity


class Task(Entity):
    @staticmethod
    def of(values: list):
        return Task(
            str(values[0]), str(values[1]), str(values[2]),
            str(values[3]), str(values[4]), str(values[5]),
            str(values[6]))

    def __init__(self, entity_id: str = None, status: str = None, name: str = None, date: str = None,
                 time: str = None, task_type: str = None, priority: str = None):
        super().__init__(entity_id)
        self.entity_id = entity_id
        self.status = status
        self.name = name
        self.date = date
        self.time = time
        self.task_type = task_type
        self.priority = priority

    def __str__(self):
        return '{}"entity_id": "{}", "status": "{}", "name": "{}", "date": "{}", "time": "{}", "task_type": "{}", ' \
               '"priority": "{}"{}'\
            .format(super().__str__(), '{', self.entity_id, self.status, self.name, self.date,
                    self.time, self.task_type, self.priority, '}')

    class Builder:
        def __init__(self):
            self.entity_id = str(uuid.uuid4())
            self.status = None
            self.name = None
            self.date = None
            self.time = None
            self.task_type = None
            self.priority = None

        def with_status(self, status: str):
            self.status = status
            return self

        def with_name(self, name: str):
            self.name = name
            return self

        def with_date(self, date: str):
            self.date = date
            return self

        def with_time(self, time: str):
            self.time = time
            return self

        def with_type(self, task_type: str):
            self.task_type = task_type
            return self

        def with_priority(self, priority: str):
            self.priority = priority
            return self

        def build(self):
            return Task(self.entity_id, self.status, self.name, self.date, self.time, self.task_type,
                        self.priority)
