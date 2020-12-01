from abc import ABC, abstractmethod
from core.model.entity import Entity


class CrudRepository(ABC):
    @abstractmethod
    def insert(self, entity: Entity):
        pass

    @abstractmethod
    def update(self, task_id, new_data):
        pass

    @abstractmethod
    def delete(self, task_id):
        pass

    @abstractmethod
    def get(self):
        pass
