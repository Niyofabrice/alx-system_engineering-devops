#!/usr/bin/python3

def number_of_subscribers(subreddit):
    """ function that returns number of subscribers for a given subreddit """
    import requests

    subreddit_info = requests.get("https://reddit.com/r/{}/about/.json".format(subreddit))
    return subreddit_info.json().get("data").get("subscribers")
