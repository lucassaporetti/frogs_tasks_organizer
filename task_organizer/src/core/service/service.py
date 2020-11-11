from abc import ABC

from core.crud.file.file_repository import MyRepo
from src.core.model.entity import Entity


class Service(ABC):
    def __init__(self):
        self.database = MyRepo('gabirubal')

    def __str__(self):
        return self.__class__.__name__

    def save(self, entity: Entity):
        if entity.uuid is None or self.database.find_by_id(entity.uuid) is None:
            self.database.insert(entity)
        else:
            self.database.update(entity)

    def remove(self, entity: Entity):
        self.database.delete(entity)

    def list(self, filters: str = None) -> list:
        return self.database.find_all(filters=filters)

    def get(self, entity_id: str) -> Entity:
        return self.database.find_by_id(entity_id)
