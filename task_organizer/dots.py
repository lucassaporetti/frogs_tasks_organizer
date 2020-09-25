import base64

with open('/home/lucassaporetti/git_repository/frogs_tasks_organizer/task_organizer/resources/green_dot.png', "rb") as f:
    data = f.read()
    print(base64.b64encode(data))

# with open('/home/lucassaporetti/git_repository/frogs_tasks_organizer/task_organizer/resources/red_dot.png', "rb") as f:
#     data = f.read()
#     print(base64.b64encode(data))

# with open('/home/lucassaporetti/git_repository/frogs_tasks_organizer/task_organizer/resources/blue_dot.png', "rb") as f:
#     data = f.read()
#     print(base64.b64encode(data))
