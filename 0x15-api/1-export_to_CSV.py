#!/usr/bin/python3
"""
a python script that retrieves using a given REST API
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    usid = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(usid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        usid)
    todo = requests.get(url, verify=False).json()
    with open("{}.csv".format(usid), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todo:
            taskwriter.writerow([int(usid), user.get('username'),
                                 t.get('completed'),
                                 t.get('title')])
