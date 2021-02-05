# import uuid
# from firebase import firebase
# import pyrebase
# from src.core.config.app_config import log
# from src.core.model.entity import Entity
# from src.core.crud.crud_repository import CrudRepository
# from src.core.crud.firebase.firebase_config import firebase_config
#
#
# class FirebaseRepository(CrudRepository):
#     def __init__(self):
#         self.logger = log
#         self.payload = None
#         self.config = firebase_config
#         self.pyrebase = pyrebase.initialize_app(firebase_config)
#         self.firebase = \
#             firebase.FirebaseApplication('https://frogs-task-organizer-d5e24.firebaseio.com', None)
#         self.db = self.pyrebase.database()
#         self.all_data = []
#
#     def __str__(self):
#         return str(self.payload)
#
#     def get(self):
#         self.logger.debug('Inserting firebase entry: GET * into: {}'
#                           .format(self.pyrebase.database_url))
#         self.all_data.clear()
#         tasks = self.db.child('tasks').get()
#         if tasks.val() is not None:
#             for task in tasks.each():
#                 self.all_data.append(task.val())
#             return self.all_data
#         else:
#             pass
#
#     def insert(self, entity: Entity):
#         entity.uuid = entity.uuid if entity.uuid is not None else str(uuid.uuid4())
#         payload = entity.to_json()
#         self.logger.debug('Inserting firebase entry: INSERT {} into: {}'
#                           .format(entity, self.pyrebase.database_url))
#         self.db.child('tasks').push(payload)
#
#     def update(self, task_id, new_data):
#         self.logger.debug('Inserting firebase entry: UPDATE status == "{}" where uuid == "{}" into: {}'
#                           .format(new_data, task_id, self.pyrebase.database_url))
#         tasks = self.db.child('tasks').get()
#         if self.all_data is not None:
#             selected_task = tasks.val()
#             for key, value in selected_task.items():
#                 if value['uuid'] == task_id:
#                     self.firebase.patch('/tasks/{}/'.format(key), {'status': '{}'.format(new_data)})
#         else:
#             pass
#
#     def delete(self, task_id):
#         self.logger.debug('Inserting firebase entry: DELETE task with uuid == "{}" into: {}'
#                           .format(task_id, self.pyrebase.database_url))
#         tasks = self.db.child('tasks').get()
#         if self.all_data is not None:
#             selected_task = tasks.val()
#             for key, value in selected_task.items():
#                 if value['uuid'] == task_id:
#                     self.firebase.delete('/tasks/{}'.format(key), None)
#         else:
#             pass
