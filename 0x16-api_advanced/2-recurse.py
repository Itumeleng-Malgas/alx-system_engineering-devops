#!/usr/bin.python3
""" Module that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Queries the Reddit API for titles of all hot articles """

    if not is_valid_subreddit(subreddit):
        return None

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'MyRedditBot/1.0 by Itumeleng-Malgas'}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])

    if not children:
        return hot_list

    for post in children:
        title = post.get('data', {}).get('title', '')
        hot_list.append(title)

    after = data.get('after')
    return recurse(subreddit, hot_list, after)

def is_valid_subreddit(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyRedditBot/1.0 by Itumeleng-Malgas'}

    response = requests.get(url, headers=headers)

    return response.status_code == 200
