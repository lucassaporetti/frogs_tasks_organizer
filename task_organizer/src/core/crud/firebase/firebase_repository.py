import uuid
import pyrebase
from src.core.config.app_config import log
from core.model.entity import Entity
from core.crud.crud_repository import CrudRepository
from core.crud.firebase.firebase_config import firebase_config


class FirebaseRepository(CrudRepository):
    def __init__(self):
        self.logger = log
        self.payload = None
        self.config = firebase_config
        self.firebase = pyrebase.initialize_app(firebase_config)
        self.db = self.firebase.database()
        self.all_data = []

    def __str__(self):
        return str(self.payload)

    def insert(self, entity: Entity):
        entity.uuid = entity.uuid if entity.uuid is not None else str(uuid.uuid4())
        payload = entity.to_json()
        self.logger.debug('Inserting firebase entry: INSERT {} into: {}'.format(entity, self.firebase.database_url))
        self.db.child('tasks').push(payload)

    def update(self, data):
        self.logger.debug('Inserting firebase entry: UPDATE {} into: {}'.format(data, self.firebase.database_url))
        tasks = self.db.child('tasks').get()
        for task in tasks.each():
            if task.uuid == data.uuid:
                self.db.child('tasks').update(data)

    def delete(self, data):
        self.logger.debug('Inserting firebase entry: DELETE {} into: {}'.format(data, self.firebase.database_url))
        tasks = self.db.child('tasks').get()
        for task in tasks.each():
            if task.uuid == data.uuid:
                self.db.child('tasks').task.uuid.remove()

    def get(self):
        self.logger.debug('Inserting firebase entry: GET * into: {}'.format(self.firebase.database_url))
        tasks = self.db.child('tasks').get()
        if tasks.val() is not None:
            for task in tasks.each():
                self.all_data.append(task.val())
            return self.all_data
