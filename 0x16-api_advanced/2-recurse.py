#!/usr/bin/python3
"""
Module that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_titles=[], after=None):
    """
    Queries the Reddit API for titles of all hot articles.
    """

    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom-Agent"}
    params = {"after": after}

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        children = response.json().get("data", {}).get("children", [])
        hot_titles += [child["data"]["title"] for child in children]

        next_after = response.json().get("data", {}).get("after")
        return (hot_titles if next_after is None else recurse(subreddit,
                hot_titles, next_after))

    return None
