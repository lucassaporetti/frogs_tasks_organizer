from abc import abstractmethod, ABC
from src.core.config.app_config import AppConfigs


class ApiFactory(ABC):
    # @staticmethod
    # def dict_to_values(values: dict) -> str:
    #     str_values = ""
    #     for key, value in values.items():
    #         if value is not None:
    #             sep = ", " if str_values else ""
    #             str_values += '{}"{}"'.format(sep, value)
    #
    #     return str_values
    #
    # @staticmethod
    # def list_to_filters(filters: list, separator=",") -> str:
    #     str_filters = ""
    #     for api_filter in filters:
    #         sep = separator if str_filters else ""
    #         parts = api_filter.strip().split("=")
    #         if len(parts) >= 2:
    #             key = parts[0].strip()
    #             value = parts[1].strip().replace('"', "")
    #             str_filters += '{} AND {}={}'.format(sep, key, value)
    #
    #     return str_filters
    #
    # @staticmethod
    # def list_to_columns(columns: list) -> str:
    #     str_columns = ""
    #     for key, value in columns:
    #         if value is not None:
    #             sep = ", " if str_columns else ""
    #             str_columns += '{}{}'.format(sep, key.upper(), value)
    #
    #     return str_columns
    #
    # @staticmethod
    # def dict_to_field_set(values: dict) -> str:
    #     str_field_set = ""
    #     for key, value in values.items():
    #         if value is not None:
    #             sep = ", " if str_field_set else ""
    #             str_field_set += '{}{} = "{}"'.format(sep, key.upper(), value)
    #
    #     return str_field_set

    def __init__(self):
        self.api_url = 'http://localhost:8000/tasks/'

    def __str__(self):
        return self.__class__.__name__

    @abstractmethod
    def get(self, url: None, columns: list = None, filters: list = None):
        pass

    @abstractmethod
    def post(self, url: None, values: dict):
        pass

    @abstractmethod
    def put(self,  url: None, values: dict = None, filters: list = None):
        pass

    @abstractmethod
    def delete(self, url: None, filters: list = None):
        pass
