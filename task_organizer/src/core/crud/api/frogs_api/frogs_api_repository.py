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

    def __str__(self):
        return "{}:{}/{}".format(self.api_url, self.status_code, self.reason)

    def test_internet_connection(self):
        try:
            internet_connector = requests.session()
            response = internet_connector.get("http://216.58.192.142")
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
