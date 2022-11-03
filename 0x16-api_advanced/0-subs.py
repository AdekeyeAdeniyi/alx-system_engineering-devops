#!/usr/bin/python3
"""
    Returns number of (not active users, total subscribers) of a Reddit Account
"""
import requests

def number_of_subscribers(subreddit):
    """
        Return total number of subscribers of a `Reddit User`

        Parameters
        ----------
            subreddit(str): reddit account user name

        Return(int):
            Number of Subscribers
    """

    response = requests.get(
        'https://www.reddit.com/r/{}/about.json?limit=10'.format(subreddit),
        headers={'User-Agent': 'Mozilla/5.0'},
        allow_redirects=False
    )

    body = response.json()

    if (response.status_code != 404):
        return (body.get('data').get('subscribers'))
    else:
        return (0)
