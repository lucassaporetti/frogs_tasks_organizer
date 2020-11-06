import uuid
import httplib2
from abc import abstractmethod
from typing import Optional
import requests
from src.model.entity_model import Entity
from src.core.factory.api_factory import ApiFactory
from src.core.repository.api.api_repository import ApiRepository
from src.core.tools.commons import print_error


class FrogsApiRepository(ApiRepository):
    __cache = {}

    def __init__(self, api_factory: ApiFactory):
        super().__init__(api_factory)
        self.api_connector = requests.session()
        self.url = api_factory.api_url()

    def __str__(self):
        return "{}:{}/{}".format(self.url, self.status_code, self.reason)

    def internet_connection(self):
        self.internet_connector = httplib2.HTTPConnectionWithTimeout("216.58.192.142", timeout=5)
        try:
            self.internet_connector.request("HEAD", "/")
            self.internet_connector.close()
            self.log.info('Internet connection: Ok')
            return True
        except httplib2.HttpLib2Error:
            self.internet_connector.close()
            self.log.error('Error: internet connection failed')
            print_error('Error: internet connection failed')
            return False

    def api_connection(self):
        if self.internet_connection() is True:
            try:
                self.api_connector.get(url=self.url)
                self.log.info('API connection: Ok')
                return True
            except requests.exceptions.RequestException:
                self.log.error('Error: API connection failed')
                print_error('Error: API connection failed')
                return False
        else:
            return False

    def insert(self, entity: Entity):
        if self.api_connection is True:
            entity.id = entity.id if entity.id is not None else str(uuid.uuid4())
            self.log.info('Executing API statement: post(url={}, json={})')\
                .format(url=self.url, json=entity.__dict__)
            api_post = self.api_connector.post(url=self.url, json=entity)
            self.status_code = api_post.status_code
            self.reason = api_post.reason
            self.log.info('HTTP response: Status Code = {}, Reason = {})')\
                .format(self.status_code, self.reason)
            if self.status_code == 200:
                self.log.info('Operation result: A new task has been saved')
                return api_post
            else:
                self.log.error('Error: New task may not have been saved correctly')
                print_error('Error: New task may not have been saved correctly')
                return api_post
        else:
            self.log.error('Error: Without connection to API')
            print_error('Error: Without connection to API')

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
    # @abstractmethod
    # def row_to_entity(self, row: tuple) -> Entity:
    #     pass
