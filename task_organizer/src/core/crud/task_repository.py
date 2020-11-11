from abc import ABC

from core.crud.file.file_repository import FileRepository
from src.core.enum.database_type import DatabaseType
from src.core.model.task_model import Task
from src.core.model.entity import Entity


class TaskRepository(FileRepository, ABC):
    def __init__(self):
        super().__init__(DatabaseType.FILE)

    def insert(self, task: Task):
        super().insert(task)

    def update(self, task: Task):
        super().update(task)

    def delete(self, task: Task):
        super().delete(task)

    @staticmethod
    def row_to_entity(row: tuple) -> Entity:
        return Task.of(list(row))
