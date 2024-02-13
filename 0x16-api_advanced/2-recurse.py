#!/usr/bin.python3
""" Module that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Queries the Reddit API for titles of all hot articles """

    if hot_list is None:
        hot_list = []

    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {'User-Agent': 'Custom-User-Agent'}
        params = {'limit': 10, 'after': after} if after else {'limit': 10}

        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])

            if not children:
                return hot_list if hot_list else None

            hot_list.extend([post.get('data', {}).get('title')
                            for post in children])

            after = data.get('after')
            return recurse(subreddit, hot_list, after)

        else:
            return None

    except Exception:
        return None
