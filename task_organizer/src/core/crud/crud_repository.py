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
    def update(self, selected_entity_id, key_to_update, new_entity_value):
        pass

    @abstractmethod
    def delete(self, entity: Entity):
        pass
