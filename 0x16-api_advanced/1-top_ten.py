#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ Function that queries the Reddit API """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom-User-Agent'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            for post in response.json()['data']['children']:
                print(post['data']['title'])
        elif response.status_code == 404:
            print(None)
    except Exception:
        print(None)
