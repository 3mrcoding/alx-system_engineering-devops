#!/usr/bin/python3
import requests
"""Construct the URL for the Reddit API endpoint"""


def number_of_subscribers(subreddit):
    """Construct the URL for the Reddit API endpoint"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        data = response.json()

        subscribers = data["data"]["subscribers"]

        return subscribers
    else:
        return 0
