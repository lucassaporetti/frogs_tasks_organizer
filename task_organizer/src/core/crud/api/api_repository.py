from abc import abstractmethod
from src.core.config.app_config import log
from src.core.crud.api.api_factory import ApiFactory
from src.core.crud.repository import Repository


class ApiRepository(Repository):
    def __init__(self, api_factory: ApiFactory):
        super().__init__(api_factory.__str__())
        self.api_factory = api_factory
        self.logger = log
        self.status_code = None
        self.reason = None
        self.internet_connector = None
        self.api_connector = None
        self.api_url = None
        self.internet_connection()
        self.api_connection()

    @abstractmethod
    def internet_connection(self):
        pass

    @abstractmethod
    def api_connection(self):
        pass
