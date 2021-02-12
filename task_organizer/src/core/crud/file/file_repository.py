import re
import uuid
from typing import Optional
from src.core.config.app_config import log
from src.core.crud.file.file_storage import FileStorage
from src.core.crud.crud_repository import CrudRepository
from src.core.model.entity import Entity


class FileRepository(CrudRepository):
    __storages = {}

    @staticmethod
    def check_criteria(partial_value, whole_value):
        if isinstance(whole_value, str):
            return str(partial_value).upper() in whole_value.upper()
        elif isinstance(whole_value, int):
            return int(partial_value) == whole_value
        elif isinstance(whole_value, float):
            return float(partial_value) == whole_value
        elif isinstance(whole_value, bool):
            return bool(partial_value) == whole_value
        else:
            return False

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
        self.logger.debug("{} has been inserted !".format(entity.__class__.__name__))

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
                self.logger.debug("{} has been updated !".format(entity.__class__.__name__))

    def delete(self, entity: Entity):
        print(entity)
        self.file_db.data.remove(entity)
        self.file_db.commit()
        self.logger.debug("{} has been deleted !".format(entity.__class__.__name__))

    def dict_to_entity(self, row: dict) -> Entity:
        return Entity(row[uuid])

    def find_by_id(self, entity_id: str) -> Optional[Entity]:
        for entity in self.file_db.data:
            if entity_id == entity['uuid']:
                return entity if len(self.file_db.data) > 0 else None
            else:
                return None

    def find_all(self, filters: str = None) -> Optional[list]:
        if filters is not None:
            file_filters = filters.split(',')
            filtered = []
            for next_filter in file_filters:
                fields = re.split('=|>|<|>=|<=|==|!=', next_filter)
                try:
                    found = [
                        self.dict_to_entity(some_entity) for some_entity in self.file_db.data if
                        self.check_criteria(fields[1], some_entity[fields[0]])
                    ]
                except KeyError:
                    continue
                except IndexError:
                    continue
                filtered.extend(found)
            return filtered
        else:
            return [self.dict_to_entity(some_entity) for some_entity in self.file_db.data]
