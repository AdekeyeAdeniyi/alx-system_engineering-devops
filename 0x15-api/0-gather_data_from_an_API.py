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
import urllib.request

employee_id = int(sys.argv[1])
url = 'https://jsonplaceholder.typicode.com'


def url_request(query, id=None):
    """ Returns data from HTTP Request
    """
    if id:
        with urllib.request.urlopen(url=f'{url}/{query}/{id}') as user_data:
            body = user_data.read()
            response = json.loads(body)
            return response
    else:
        with urllib.request.urlopen(url=f'{url}/{query}/') as user_data:
            body = user_data.read()
            response = json.loads(body)
            return response


if __name__ == '__main__':
    if employee_id:
        empolyee = url_request("users", employee_id)
        todos = url_request("todos")

        empolyee_name = empolyee.get('name')
        tasks = list(filter(lambda x: x.get('userId') == employee_id, todos))
        completed_task = list(filter(lambda x: x.get('completed'), tasks))
        completed_task_no = len(completed_task)
        total_task = len(tasks)

        print('Employee {} is done with tasks({}/{}):'.format(
            empolyee_name,
            completed_task_no,
            total_task
        ))

        if completed_task_no:
            for task in completed_task:
                print('\t', task.get('title'))
