import uuid
import httplib2
from abc import abstractmethod
from typing import Optional
import requests
import json
from core.crud.api import api_factory
from src.core.model.entity import Entity
from src.core.crud.api.api_factory import ApiFactory
from src.core.crud.api.api_repository import ApiRepository
from typing import Optional

import requests
from requests.structures import CaseInsensitiveDict


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
        self.api_connector = requests.Session()
        self.url = 'localhost:8000'

    def __str__(self):
        return "{}:{}/{}".format(self.url, self.status_code, self.reason)

    def internet_connection(self):
        self.internet_connector = httplib2.HTTPConnectionWithTimeout("216.58.192.142", timeout=5)
        try:
            self.internet_connector.request("HEAD", "/")
            self.internet_connector.close()
            self.logger.info('Internet connection: Ok')
            return True
        except httplib2.HttpLib2Error:
            self.internet_connector.close()
            self.logger.error('Error: internet connection failed')
            return False

    def api_connection(self):
        test_internet_connection = self.internet_connection()
        if test_internet_connection is True:
            try:
                requests.get(url='http://127.0.0.1:8000/')
                self.logger.info('API connection: Ok')
                return True
            except requests.exceptions.RequestException:
                self.logger.error('Error: API connection failed')
                return False
        else:
            return False

    def insert(self, entity: Entity):
        # test_api_connection = self.api_connection()
        # if test_api_connection is True:
        entity.uuid = str(uuid.uuid4())
        self.logger.info('Processing REST {} -> {}'.format('POST', self.api_url))
        data = entity.to_json()
        url = 'http://127.0.0.1:8000/tasks/'
        print(data)
        response = requests.post(url=url, json=data)
        self.logger.info('Response <=  Status: {}  Payload: {}'.format(response.status_code, response.reason))
        if 299 <= response.status_code >= 200:
            self.logger.info('Operation result: A new task has been saved')
        else:
            self.logger.error('Error: New task may not have been saved correctly')
    # else:
    #     self.logger.error('Error: Without connection to API')

    # def insert(self, entity: Entity):
    #     if self.api_connection is True:
    #         entity.uuid = str(uuid.uuid4())
    #         self.logger.info('Executing API statement: post(url={}, json={})')\
    #             .format(url=self.url, json=entity.__dict__)
    #         api_post = self.api_connector.post(url=self.url, json=entity)
    #         self.status_code = api_post.status_code
    #         self.reason = api_post.reason
    #         self.logger.info('HTTP response: Status Code = {}, Reason = {})')\
    #             .format(self.status_code, self.reason)
    #         if self.status_code == 200:
    #             self.logger.info('Operation result: A new task has been saved')
    #             return api_post
    #         else:
    #             self.logger.error('Error: New task may not have been saved correctly')
    #             return api_post
    #     else:
    #         self.logger.error('Error: Without connection to API')

    # def put(self, entity: Entity):
    #     update_stm = self.sql_factory.update(entity.__dict__, filters=[
    #         "ENTITY_ID = '{}'".format(entity.entity_id)
    #     ])
    #     self.log.info('Executing SQL statement: {}'.format(update_stm))
    #     self.cursor.execute(update_stm)
    #     self.connector.commit()
    #
    # def delete(self, entity: Entity):
    #     delete_stm = self.sql_factory.delete(filters=[
    #         "ENTITY_ID = '{}'".format(entity.entity_id)
    #     ])
    #     self.log.info('Executing SQL statement: {}'.format(delete_stm))
    #     self.cursor.execute(delete_stm)
    #     self.connector.commit()
    #
    # def find_all(self, filters: str = None) -> Optional[list]:
    #     if filters is not None:
    #         sql_filters = filters.upper().split(',')
    #     else:
    #         sql_filters = None
    #     select_stm = self.sql_factory.select(filters=sql_filters)
    #     self.log.info('Executing SQL statement: {}'.format(select_stm))
    #     try:
    #         self.cursor.execute(select_stm)
    #         result = self.cursor.fetchall()
    #         ret_val = []
    #         for next_row in result:
    #             ret_val.append(self.row_to_entity(next_row))
    #         return ret_val
    #     except ProgrammingError:
    #         return None
    #
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
    #

    @abstractmethod
    def dict_to_entity(self, row: dict) -> Entity:
        pass


class MyApiRepo(FrogsApiRepository):
    def __init__(self):
        super().__init__()

    def dict_to_entity(self, row: dict) -> Entity:
        return Entity(row[uuid])
