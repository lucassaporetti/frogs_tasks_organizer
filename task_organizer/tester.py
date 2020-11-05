import requests

connector = requests.session()

try:
    connection = connector.get(url="http://localhost:8000/tasks/")
    print('ok')
    print(connection.json())
except requests.exceptions.RequestException:
    (print('Error'))
