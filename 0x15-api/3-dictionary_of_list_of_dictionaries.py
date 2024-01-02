#!/usr/bin/python3
'''
a python script to export data in the JSON format
'''
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(url, verify=False).json()
    undoc = {}
    udoc = {}
    for user in user:
        usid = user.get("id")
        udoc[usid] = []
        undoc[usid] = user.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    todo = requests.get(url, verify=False).json()
    [udoc.get(tsk.get("userId")).append({"task": tsk.get("title"),
                                       "completed": tsk.get("completed"),
                                       "username": undoc.get(
        tsk.get("userId"))})
     for tsk in todo]
    with open("todo_all_employees.json", 'w') as jsf:
        json.dump(udoc, jsf)
