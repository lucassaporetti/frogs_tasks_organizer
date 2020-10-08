from src.core.enum.model_enum import Model
from src.core.enum.repository_type import RepositoryType
from src.core.service.service import Service
from src.model.task_model import Task


class TaskService(Service):
    def __init__(self, repository_type: RepositoryType):
        super().__init__(repository_type, Model.TASK)

    def save(self, task: Task):
        super().save(task)

    def remove(self, task: Task):
        super().remove(task)

    def get(self, id: str) -> Task:
        entity = super().get(id)
        task = Task()
        task.__dict__ = entity.__dict__
        return task
