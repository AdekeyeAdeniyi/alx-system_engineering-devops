#!/usr/bin/python3
"""
    Python Script that prints
        - Employee Name
        - Completed task / Total task
        - Lists of completed task
    using a REST API and Empolyee ID.
"""
import re
import sys
import requests

url = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    if len(sys.argv) > 0:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employee_id = int(sys.argv[1])
            empolyee = requests.get(f'{url}/users/{employee_id}').json()
            todos = requests.get(f'{url}/todos').json()

            tasks = list(filter(lambda x: x.get('userId') == employee_id, todos))
            completed_task = list(filter(lambda x: x.get('completed'), tasks))

            print('Employee {} is done with tasks({}/{}):'.format(
                empolyee.get('name'),
                len(completed_task),
                len(tasks)
            ))

            if  len(completed_task) > 0:
                for task in completed_task:
                    print('\t', task.get('title'))
