#!/usr/bin/python3
"""
Module that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, keyword_list, found_list=[], after=None):
    """ Function that count keywords in hot posts titles """
    user_agent = {'User-Agent': 'Test100'}
    base_url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    response = requests.get(base_url, headers=user_agent)

    if after is None:
        keyword_list = [keyword.lower() for keyword in keyword_list]

    if response.status_code == 200:
        data = response.json()['data']
        after_token = data['after']
        posts = data['children']

        found_list.extend([
            word for post in posts
            for word in post['data']['title'].lower().split(' ')
            if word in keyword_list
        ])

        if after_token is not None:
            count_words(subreddit, keyword_list, found_list, after_token)
        else:
            result = {word.lower(): found_list.count(word.lower())
                      for word in set(found_list)}
            sorted_result = sorted(result.items(), key=lambda item: item[1],
                                   reverse=True)

            for key, value in sorted_result:
                print(f'{key}: {value}')
    else:
        return
