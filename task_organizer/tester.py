from hspylib.core.tools.table_renderer import TableRenderer

#
# connector = requests.session()
#
# try:
#     connection = connector.get(url="http://localhost:8000/tasks/")
#     print('ok')
#     print(connection.json())
# except requests.exceptions.RequestException:
#     (print('Error'))

if __name__ == '__main__':
    h = [
        'Col 1',
        'Columns 2',
        'Columns 3',
        'Thats a big Column Header'
    ]
    data = [
        ('One', 1, True, 2),
        ('Two', 2, False, 3),
        ('Three, four and five', 3, True, 3),
    ]
    tr = TableRenderer(h, data, 'TableRenderer example of usage')
    tr.render()

