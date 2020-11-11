from src.core.service.service import Service
from src.core.model.task_model import Task


class TaskService(Service):
    def __init__(self):
        super().__init__()

    def save(self, task: Task):
        super().save(task)

    def remove(self, task: Task):
        super().remove(task)

    def get(self, entity_id: str) -> Task:
        entity = super().get(entity_id)
        task = Task()
        task.__dict__ = entity.__dict__
        return task
