#!/usr/bin/python3
"""
a python script that retrieves using a given REST API
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])

    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    todo_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))

    if user_response.status_code != 200:
        print("User not found")
        exit(1)

    user_data = user_response.json()
    todo_data = todo_response.json()

    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]
    for task in todo_data:
        csv_data.append([user_data['id'], user_data['username'],
                        str(task['completed']), task['title']])

    csv_file_name = "{}.csv".format(user_data['id'])
    with open(csv_file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(csv_data)

    print("CSV file '{}' has been created.".format(csv_file_name))
