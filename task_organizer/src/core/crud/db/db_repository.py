from abc import abstractmethod
from typing import Tuple

from src.core.config.app_config import AppConfigs
from src.core.crud.repository import Repository
from src.core.model.entity import Entity


class DBRepository(Repository):
    def __init__(self):
        super().__init__()
        self.hostname = AppConfigs.INSTANCE.get('datasource.hostname')
        self.port = AppConfigs.INSTANCE.get_int('datasource.port')
        self.user = AppConfigs.INSTANCE.get('datasource.username')
        self.password = AppConfigs.INSTANCE.get('datasource.password')
        self.database = AppConfigs.INSTANCE.get('datasource.database')
        self.logger = AppConfigs.INSTANCE.logger()

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
    def execute(self, sql_statement: str, auto_commit: bool = True, *params):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass

    @abstractmethod
    def row_to_entity(self, row: Tuple) -> Entity:
        pass

    @abstractmethod
    def table_name(self) -> str:
        pass