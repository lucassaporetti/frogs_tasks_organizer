from abc import abstractmethod
from src.core.config.app_configs import AppConfigs
from src.core.tools.commons import log_init
from src.core.factory.api_factory import ApiFactory
from src.core.repository.repository import Repository


class ApiRepository(Repository):
    def __init__(self, api_factory: ApiFactory):
        super().__init__(api_factory.__str__())
        self.api_factory = api_factory
        self.log = log_init(AppConfigs.log_file())
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
