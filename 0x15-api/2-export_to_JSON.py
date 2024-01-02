#!/usr/bin/python3
'''
a python script to export data in the JSON format.
'''

import json
import requests
from sys import argv

if __name__ == '__main__':
    usid = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(usid)
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(usid)
    user = requests.get(url, verify=False).json()
    todo = requests.get(url, verify=False).json()
    name = user.get('username')
    tsk = [{"task": tsk.get("title"),
          "username": name,
          "completed": tsk.get("completed")} for tsk in todo]
    bj = {}
    bj[usid] = tsk
    with open("{}.json".format(usid), 'w') as filejs:
        json.dump(bj, filejs)
