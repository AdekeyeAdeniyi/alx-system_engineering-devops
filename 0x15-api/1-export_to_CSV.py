#!/usr/bin/python3
"""
Python Script that create a CSV file that contains
empolyee_id
empolyee_name
task_completed
empolyee title
"""
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
        with open('{}.csv'.format(id), mode='w') as employee_file:
            if len(tasks) > 0:
                for task in tasks:
                    employee_file.write('"{}","{}","{}","{}"\n'.format(
                        id,
                        empolyee.get('name'),
                        task.get('completed'),
                        task.get('title')
                    ))
