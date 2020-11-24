from abc import ABC, abstractmethod
from core.model.entity import Entity


class CrudRepository(ABC):
    @abstractmethod
    def insert(self, entity: Entity):
        pass

    @abstractmethod
    def update(self, data):
        pass

    @abstractmethod
    def delete(self, data):
        pass

    @abstractmethod
    def get(self):
        pass
