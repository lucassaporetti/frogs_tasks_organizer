from src.core.factory.api_restful.frogs_api_factory import FrogsApiFactory


class TaskFactory(FrogsApiFactory):

    api_template_file = "api/task_templates.properties"

    def __init__(self):
        super().__init__(TaskFactory.api_template_file)
