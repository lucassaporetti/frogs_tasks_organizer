import uuid
from src.core.config.app_config import log
from src.core.crud.file.file_storage import FileStorage
from src.core.crud.crud_repository import CrudRepository
from src.core.model.entity import Entity


class FileRepository(CrudRepository):
    __storages = {}

    def __init__(self, filename: str):
        super().__init__()
        self.logger = log
        self.filename = filename
        self.file_db = self.read()

    def __str__(self):
        return str(self.file_db.data)

    def create(self, entity: Entity):
        entity.uuid = str(uuid.uuid4())
        self.file_db.data.append(entity.to_json())
        self.file_db.commit()
        self.logger.debug("A new {} has been inserted !".format(entity.__class__.__name__))

    def read(self):
        if self.filename in FileRepository.__storages:
            return FileRepository.__storages[self.filename]
        else:
            FileRepository.__storages[self.filename] = FileStorage(self.filename)
            return FileRepository.__storages[self.filename]

    def update(self, selected_entity_id, key_to_update, new_entity_value):
        for entity in self.file_db.data:
            if entity['uuid'] == selected_entity_id:
                entity[str('{}'.format(key_to_update))] = str('{}'.format(new_entity_value))
                self.file_db.commit()
                self.logger.debug("Task {} has been updated !".format(entity['uuid']))

    def delete(self, selected_entity_id):
        for entity in self.file_db.data:
            if entity['uuid'] == selected_entity_id:
                self.file_db.data.remove(entity)
                self.file_db.commit()
                self.logger.debug("Task {} has been deleted !".format(entity['uuid']))

    # def find_by_id(self, selected_entity_id):
    #     for entity in self.file_db.data:
    #         if entity['uuid'] == selected_entity_id:
    #             return entity
    #         else:
    #             pass
