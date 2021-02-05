from abc import ABC, abstractmethod
from typing import Optional
from src.core.model.entity import Entity


class CrudRepository(ABC):

    @abstractmethod
    def create(self, entity: Entity):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def update(self, entity: Entity):
        pass

    @abstractmethod
    def delete(self, entity: Entity):
        pass

    @abstractmethod
    def dict_to_entity(self, row: dict) -> Entity:
        pass

    @abstractmethod
    def find_by_id(self, entity_id: str) -> Optional[Entity]:
        pass

    @abstractmethod
    def find_all(self, filters: str = None) -> Optional[list]:
        pass
