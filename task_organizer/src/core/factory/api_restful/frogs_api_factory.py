from src.core.factory.api_factory import ApiFactory


class FrogsApiFactory(ApiFactory):
    def __init__(self, api_template_file: str):
        super().__init__(api_template_file)

    def count(self):
        return self.api_templates.get('COUNT')

    def insert(self, values: dict):
        return self.api_templates.get('INSERT').format(ApiFactory.dict_to_values(values))

    def update(self,  values: dict = None, filters: list = None):
        return self.api_templates.get('UPDATE')\
            .format(
                ApiFactory.dict_to_field_set(values) if values is not None else '',
                ApiFactory.list_to_filters(filters, separator='') if filters is not None else '',
            )

    def delete(self, filters: list = None):
        return self.api_templates.get('DELETE')\
            .format(
                ApiFactory.list_to_filters(filters, separator='') if filters is not None else '',
            )

    def select(self, columns: list = None, filters: list = None):
        return self.api_templates.get('SELECT')\
            .format(
                ApiFactory.list_to_columns(columns) if columns is not None else '*',
                ApiFactory.list_to_filters(filters, separator='') if filters is not None else '',
            )
