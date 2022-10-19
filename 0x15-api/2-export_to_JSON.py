#!/usr/bin/python3
"""
Python Script that create a JSON file that contains
empolyee_id
empolyee_username
task_completed
empolyee title
"""
import json
import re
import requests
import sys

API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 0:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            empolyee = requests.get('{}/users/{}'.format(API, id)).json()
            todos = requests.get('{}/todos'.format(API)).json()
            tasks = list(filter(lambda x: x.get('userId') == id, todos))
            username = empolyee.get('username')
            with open('{}.json'.format(id), mode='w') as empolyee_file:
                user_data = list(map(
                    lambda x: {
                        "task": x.get('title'),
                        "completed": x.get('completed'),
                        "username": username
                    }, tasks
                ))

                data = {
                    id: user_data
                }
                json.dump(data, empolyee_file)
