from abc import ABC, abstractmethod
from typing import Optional

from src.core.model.entity import Entity


class CrudService(ABC):
    @abstractmethod
    def save(self, entity: Entity):
        pass

    @abstractmethod
    def remove(self, entity: Entity):
        pass

    @abstractmethod
    def list(self, filters: str = None) -> Optional[list]:
        pass

    @abstractmethod
    def get(self, uuid: str) -> Optional[Entity]:
        pass
