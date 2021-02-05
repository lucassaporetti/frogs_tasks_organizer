# from abc import abstractmethod
# from src.core.config.app_config import log
# from src.core.crud.api.api_factory import ApiFactory
# from src.core.crud.crud_repository import CrudRepository
#
#
# class ApiRepository(CrudRepository):
#     def __init__(self, api_factory: ApiFactory):
#         super().__init__()
#         self.api_factory = api_factory
#         self.logger = log
#         self.status_code = None
#         self.reason = None
#         self.internet_connection = False
#         self.internet_url = 'http://216.58.192.142'
#         self.api_connection = False
#         self.api_url = 'http://127.0.0.1:8000/tasks/'
#         self.test_internet_connection()
#         self.test_api_connection()
#
#     @abstractmethod
#     def test_internet_connection(self):
#         pass
#
#     @abstractmethod
#     def test_api_connection(self):
#         pass
