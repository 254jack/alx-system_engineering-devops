#!/usr/bin/python3
"""
a python script that retrieves user data using REST API
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    e_id = int(argv[1])

    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(e_id))
    todo_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(e_id))

    if user_response.status_code != 200:
        print("User not found")
        exit(1)

    user_data = user_response.json()
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    completed_tasks = sum(task['completed'] for task in todo_data)

    print("Employee {} is done with tasks({}/{}):".format(
        user_data['name'], completed_tasks, total_tasks))

    for task in todo_data:
        if task['completed']:
            print("\t {}".format(task['title']))
