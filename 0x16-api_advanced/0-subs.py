#!/usr/bin/python3
"""
    Returns number of (not active users, total subscribers) of a Reddit Account
"""
from requests import get
from sys import argv

subreddit = argv[1]
headers = {'User-Agent': 'Mozilla/5.0'}


def number_of_subscribers(subreddit):
    """
        Return total number of subscribers of a `Reddit User`

        Parameters
        ----------
            subreddit(str): reddit account user name

        Return(int):
            Number of Subscribers
    """

    response = get(
        'https://www.reddit.com/r/{}/about.json?limit=10'.format(subreddit),
        headers=headers,
    )

    body = response.json()

    if (response.status_code != 404):
        return (body['data']['subscribers'])
    else:
        return (0)
