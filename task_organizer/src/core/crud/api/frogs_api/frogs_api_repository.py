import uuid
from abc import abstractmethod
from src.core.model.entity import Entity
from src.core.crud.api.api_factory import ApiFactory
from src.core.crud.api.api_repository import ApiRepository
import requests


class FrogsApiRepository(ApiRepository):
    __cache = {}

    @staticmethod
    def check_criteria(partial_value, whole_value):
        if isinstance(whole_value, str):
            return str(partial_value).upper() in whole_value.upper()
        elif isinstance(whole_value, int):
            return int(partial_value) == whole_value
        elif isinstance(whole_value, float):
            return float(partial_value) == whole_value
        elif isinstance(whole_value, bool):
            return bool(partial_value) == whole_value
        else:
            return False

    def __init__(self):
        super().__init__(ApiFactory())

    def __str__(self):
        return "{}:{}/{}".format(self.api_url, self.status_code, self.reason)

    def test_internet_connection(self):
        try:
            internet_connector = requests.session()
            response = internet_connector.get(self.internet_url)
            if 200 <= response.status_code <= 299:
                self.internet_connection = True
                return self.logger.info('Internet connection: Ok')
        except requests.exceptions.RequestException:
            self.internet_connection = False
            return self.logger.error('Error: Internet connection failed')

    def test_api_connection(self):
        if self.internet_connection is True:
            try:
                requests.get(url=self.api_url)
                self.api_connection = True
                return self.logger.info('API connection: Ok')
            except requests.exceptions.RequestException:
                self.api_connection = False
                return self.logger.error('Error: API connection failed')

    def insert(self, entity: Entity):
        if self.api_connection is True:
            entity.uuid = str(uuid.uuid4())
            self.logger.info('Processing REST {} -> {}'.format('POST', self.api_url))
            data = entity.to_json()
            response = requests.post(url=self.api_url, json=data)
            self.logger.info('Response <=  Status: {}  Payload: {}'.format(response.status_code, response.reason))
            if 200 <= response.status_code <= 299:
                self.logger.info('Operation result: A new task has been saved')
            else:
                self.logger.error('Error: New task may not have been saved correctly')
            self.logger.info('Task saved: {}'.format(entity))
        else:
            self.logger.error("Error: New task can't be saved")

    def update(self, entity: Entity):
        if self.api_connection is True:
            self.logger.info('Processing REST {} -> {}'.format('PUT', self.api_url))
            data = entity.to_json()
            response = requests.put(url='{}/{}'.format(self.api_url, entity.uuid), json=data)
            self.logger.info('Response <=  Status: {}  Payload: {}'.format(response.status_code, response.reason))
            if 200 <= response.status_code <= 299:
                self.logger.info('Operation result: A new task has been saved')
            else:
                self.logger.error('Error: New task may not have been saved correctly')
            self.logger.info('Task updated: {}'.format(entity))
        else:
            self.logger.error("Error: New task can't be updated")

    def delete(self, entity: Entity):
        if self.api_connection is True:
            self.logger.info('Processing REST {} -> {}'.format('DELETE', self.api_url))
            data = entity.to_json()
            response = requests.delete(url='{}/{}'.format(self.api_url, entity.uuid), json=data)
            self.logger.info('Response <=  Status: {}  Payload: {}'.format(response.status_code, response.reason))
            if 200 <= response.status_code <= 299:
                self.logger.info('Operation result: Task correctly removed')
            else:
                self.logger.error('Error: Task must not have been removed correctly')
            self.logger.info('Task deleted: {}'.format(entity))
        else:
            self.logger.error("Error: New task can't be deleted")

    def find_all(self):
        try:
            api_connector = requests.session()
            response = api_connector.get(self.api_url)
            if 200 <= response.status_code <= 299:
                data = response.json()
                self.logger.info('Data loaded correctly from API')
                return data
        except requests.exceptions.RequestException:
            data = None
            return data and self.logger.error("Error: Data can't be loaded from API")

    # def find_by_id(self, id: str) -> Optional[Entity]:
    #     if id:
    #         select_stm = self.sql_factory.select(filters=[
    #             "ENTITY_ID = '{}'".format(entity_id)
    #         ])
    #         self.log.info('Executing SQL statement: {}'.format(select_stm))
    #         self.cursor.execute(select_stm)
    #         result = self.cursor.fetchall()
    #         return self.row_to_entity(result[0]) if len(result) > 0 else None
    #     else:
    #         return None

    @abstractmethod
    def dict_to_entity(self, row: dict) -> Entity:
        pass


class MyApiRepo(FrogsApiRepository):
    def __init__(self):
        super().__init__()

    def dict_to_entity(self, row: dict) -> Entity:
        return Entity(row[uuid])
