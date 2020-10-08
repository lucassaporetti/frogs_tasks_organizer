from src.core.enum.repository_type import RepositoryType
from src.core.enum.model_enum import Model
from src.core.repository.api.frogs_api.frogs_api_repository import FrogsApiRepository
from src.model.task_model import Task
from src.model.entity_model import Entity


class TaskRepository(FrogsApiRepository):
    def __init__(self):
        super().__init__(SqlFactoryFacade.get(DatabaseType.MYSQL, Model.ITEM))

    def insert(self, task: Task):
        super().insert(task)

    def update(self, task: Task):
        super().update(task)

    def delete(self, task: Task):
        super().delete(task)

    def row_to_entity(self, row: tuple) -> Entity:
        return Task.of(list(row))
