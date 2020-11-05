from abc import ABC
from src.core.enum.repository_type import RepositoryType
from src.core.enum.model_enum import Model
from src.core.repository.repository_facade import RepositoryFacade
from src.model.entity_model import Entity


class Service(ABC):
    def __init__(self, repository_type: RepositoryType, model: Model):
        self.repository = RepositoryFacade.get(repository_type, model)

    def __str__(self):
        return self.__class__.__name__

    def save(self, entity: Entity):
        if entity.id is None or self.repository.find_by_id(entity.id) is None:
            self.repository.insert(entity)
        else:
            self.repository.update(entity)

    def remove(self, entity: Entity):
        self.repository.delete(entity)

    def list(self, filters: str = None) -> list:
        return self.repository.find_all(filters=filters)

    def get(self, id: str) -> Entity:
        return self.repository.find_by_id(id)
