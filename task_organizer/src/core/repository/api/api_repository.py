from abc import abstractmethod
from core.config.app_configs import AppConfigs
from core.tool.commons import log_init
from src.core.factory.api_factory import ApiFactory
from src.core.repository.repository import Repository


class ApiRepository(Repository):
    def __init__(self, api_factory: ApiFactory):
        super().__init__(api_factory.api_template_file)
        self.sql_factory = api_factory
        self.hostname = AppConfigs.get('db.hostname')
        self.port = AppConfigs.get_int('db.port')
        self.user = AppConfigs.get('db.user')
        self.password = AppConfigs.get('db.password')
        self.database = AppConfigs.get('db.database')
        self.log = log_init(AppConfigs.log_file())
        self.connector = None
        self.cursor = None
        self.connect()

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def is_connected(self):
        pass

    @abstractmethod
    def count(self):
        pass
