#!/usr/bin.python3
""" Module that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """ Queries the Reddit API for titles of all hot articles """
    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        headers = {'User-Agent': 'Custom-User-Agent'}
        params = {'after': after} if after else {}

        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])

            if not children:
                return hot_list if hot_list else None

            for post in children:
                hot_list.append(post.get('data', {}).get('title'))

            after = data.get('after')
            return recurse(subreddit, hot_list, after)

        elif response.status_code == 404:
            return None

    except Exception as e:
        return None
