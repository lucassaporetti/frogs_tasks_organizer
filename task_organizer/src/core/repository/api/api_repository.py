from abc import abstractmethod
from src.core.config.app_configs import AppConfigs
from src.core.tools.commons import log_init
from src.core.factory.api_factory import ApiFactory
from src.core.repository.repository import Repository


class ApiRepository(Repository):
    def __init__(self, api_factory: ApiFactory):
        super().__init__(api_factory.api_template_file)
        self.api_factory = api_factory
        self.url = AppConfigs.get('url')
        self.log = log_init(AppConfigs.log_file())
        self.response = None
        self.status_code = None
        self.reason = None
        self.connect()

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def is_connected(self):
        pass
