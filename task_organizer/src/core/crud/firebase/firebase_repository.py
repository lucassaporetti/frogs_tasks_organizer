import uuid
from firebase import firebase
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
        self.pyrebase = pyrebase.initialize_app(firebase_config)
        self.firebase = firebase.FirebaseApplication('https://frogs-task-organizer-d5e24.firebaseio.com', None)
        self.db = self.pyrebase.database()
        self.all_data = []

    def __str__(self):
        return str(self.payload)

    def insert(self, entity: Entity):
        entity.uuid = entity.uuid if entity.uuid is not None else str(uuid.uuid4())
        payload = entity.to_json()
        self.logger.debug('Inserting firebase entry: INSERT {} into: {}'.format(entity, self.pyrebase.database_url))
        self.db.child('tasks').push(payload)

    def update(self, task_id):
        self.logger.debug('Inserting firebase entry: UPDATE {} into: {}'.format(task_id, self.pyrebase.database_url))
        tasks = self.db.child('tasks').get()
        selected_task = tasks.val()
        for key, value in selected_task.items():
            if value['uuid'] == task_id:
                self.db.child('tasks').update(task_id)

    def delete(self, task_id):
        self.logger.debug('Inserting firebase entry: DELETE {} into: {}'.format(task_id, self.pyrebase.database_url))
        tasks = self.db.child('tasks').get()
        selected_task = tasks.val()
        for key, value in selected_task.items():
            if value['uuid'] == task_id:
                self.firebase.delete('/tasks/{}'.format(key), None)

    def get(self):
        self.logger.debug('Inserting firebase entry: GET * into: {}'.format(self.pyrebase.database_url))
        tasks = self.db.child('tasks').get()
        if tasks.val() is not None:
            for task in tasks.each():
                self.all_data.append(task.val())
            return self.all_data
