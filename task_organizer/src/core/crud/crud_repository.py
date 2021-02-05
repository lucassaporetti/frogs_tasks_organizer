from abc import ABC, abstractmethod
from src.core.model.entity import Entity


class CrudRepository(ABC):
    @abstractmethod
    def insert(self, entity: Entity):
        pass

    @abstractmethod
    def update(self, entity: Entity, data_key, data_value):
        pass

    @abstractmethod
    def delete(self, entoty: Entity):
        pass

    @abstractmethod
    def get(self):
        pass
