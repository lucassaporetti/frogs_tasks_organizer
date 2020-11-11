from core.crud.api.frogs_api.frogs_api_repository import FrogsApiRepository, MyApiRepo
from core.crud.crud_service import CrudService
from core.crud.file.file_repository import MyRepo
from src.core.model.entity import Entity


class Service(CrudService):
    def __init__(self):
        self.database = MyApiRepo()

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
