#!/usr/bin/python3
"""
Module that that queries the Reddit API and returns the
number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ Get the number of Reddit subscribers """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45"
               "Safari/537.36"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
