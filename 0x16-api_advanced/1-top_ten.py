#!/usr/bin/python3
"""
    Returns first `10` posts of a Reddit account
"""
import requests


def top_ten(subreddit):
    """
        Print first `10` posts of a `Reddit User`

        Parameters
        ----------
            subreddit(str): reddit account user name
    """
    response = requests.get(
        'https://www.reddit.com/r/{}/top.json'.format(subreddit),
        headers={'User-Agent': 'Mozilla/5.0'},
        allow_redirects=False,
        params={'limit': 10}
    )
    if (response.status_code == 200):
        posts = response.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    else:
        print(None)
