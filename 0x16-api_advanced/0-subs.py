#!/usr/bin/python3
"""A python script that gets the number of subscribers for a subreddit"""
import json
import requests


def number_of_subscribers(subreddit):
    """Method that requests the number of subscribers for a subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    USER_AGENT = "com.holbertonschool.myredditscript:0.0.1 (by /u/dmaring)"
    headers = {'User-Agent': USER_AGENT}
    r = requests.get(url, headers=headers)
    if (r.status_code is not 200):
        return(0)
    r = r.json()
    return(r['data']['subscribers'])
