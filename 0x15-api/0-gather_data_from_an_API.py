#!/usr/bin/python3
"""
    Python Script that prints
        - Employee Name
        - Completed task / Total task
        - Lists of completed task
    using a REST API and Empolyee ID.
"""

import json
import sys
from urllib.request import urlopen

employee_id = int(sys.argv[1])
url = 'https://jsonplaceholder.typicode.com'


def url_request(query, id=None):
    """ Returns data from HTTP Request
    """
    if id:
        with urlopen(url=f'{url}/{query}/{id}') as user_data:
            body = user_data.read()
            response = json.loads(body)
            return response
    else:
        with urlopen(url=f'{url}/{query}/') as user_data:
            body = user_data.read()
            response = json.loads(body)
            return response


if __name__ == '__main__':
    if employee_id:
        empolyee = url_request("users", employee_id)
        todos = url_request("todos")

        empolyee_name = empolyee['name']
        tasks = list(filter(lambda x: x['userId'] == 2, todos))
        completed_task = list(filter(lambda x: x['completed'], tasks))
        completed_task_no = len(completed_task)
        total_task = len(tasks)

        print('Employee {} is done with tasks({}/{}):'.format(
            empolyee_name,
            completed_task_no,
            total_task
        ))

        if completed_task_no:
            for task in completed_task:
                print('\t', task['title'])
