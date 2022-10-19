#!/usr/bin/python3
"""
Python Script that create a JSON file that contains
empolyee_id
empolyee_username
task_completed
empolyee title (All)
"""
import json
import re
import requests

API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    empolyees = requests.get('{}/users'.format(API)).json()
    todos = requests.get('{}/todos'.format(API)).json()

    data = {}

    for empolyee in empolyees:
        id = empolyee.get('id')
        tasks = list(filter(lambda x: x.get('userId') == id, todos))
        username = empolyee.get('username')

        user_data = list(map(
            lambda x: {
                "username": username,
                "task": x.get('title'),
                "completed": x.get('completed')
            }, tasks
        ))

        data[id] = user_data
    with open('todo_all_employees.json', mode='w') as all_employees_file:
        json.dump(data, all_employees_file)
