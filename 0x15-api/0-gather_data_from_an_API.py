#!/usr/bin/python3
'''
a python script that returns information using REST API
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, user))
        name = req.json().get("name")
        if name is not None:
            kreq = requests.get(
                "{}todos?userId={}".format(
                    url, user)).json()
            alltsk = len(kreq)
            comptask = []
            for t in kreq:
                if t.get("completed") is True:
                    comptask.append(t)
            count = len(comptask)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, count, alltsk))
            for title in comptask:
                print("\t {}".format(title.get("title")))
