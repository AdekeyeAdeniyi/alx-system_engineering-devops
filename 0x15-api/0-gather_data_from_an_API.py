#!/usr/bin/python3
"""
Python Script that prints
Employee Name
Completed task / Total task
Lists of completed task
using a REST API and Empolyee ID.
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
            completed_task = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    empolyee.get('name'),
                    len(completed_task),
                    len(tasks)
                )
            )
            for task in completed_task:
                print('\t {}'.format(task.get('title')))
