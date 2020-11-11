# from hspylib.core.tools.table_renderer import TableRenderer

#
# connector = requests.session()
#
# try:
#     connection = connector.get(url="http://localhost:8000/tasks/")
#     print('ok')
#     print(connection.json())
# except requests.exceptions.RequestException:
#     (print('Error'))
#
# if __name__ == '__main__':
#     h = [
#         'Col 1',
#         'Columns 2',
#         'Columns 3',
#         'Thats a big Column Header'
#     ]
#     data = [
#         ('One', 1, True, 2),
#         ('Two', 2, False, 3),
#         ('Three, four and five', 3, True, 3),
#     ]
#     tr = TableRenderer(h, data, 'TableRenderer example of usage')
#     tr.render()
import requests

url = 'http://127.0.0.1:8000/tasks/'

data = {"uuid": "0309799d-67c8-427b-9359-0817c6e30a7d", "status": "To do", "name": "foiiiiiiiiiiiiiiiiiiiiiiii", "date": "2020/11/10", "time": "23:20", "task_type": "Business", "priority": "IMPORTANT / URGENT"}

response = requests.post(url=url, json=data)
print(response.status_code, response.reason)
