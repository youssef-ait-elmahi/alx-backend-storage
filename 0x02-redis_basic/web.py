#!/usr/bin/env python3
"""
This module provides a function to get the HTML content of a URL and cache it.
"""

import requests
from redis import Redis
from functools import wraps
from typing import Callable

# create a Redis client
redis = Redis()

def cache_page(func: Callable) -> Callable:
    """
    Decorator to cache the HTML content of a URL with an expiration time of 10 seconds.
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        # get the cache key for the url
        key = f"cached:{url}"
        # get the count key for the url
        count_key = f"count:{url}"
        # increment the count by 1
        redis.incr(count_key)
        # get the cached response from the cache
        cached_response = redis.get(key)
        # if the cache is empty, call the original function
        if not cached_response:
            response = func(url)
            # cache the response with a 10-second expiry
            redis.set(key, response, ex=10)
            return response
        # otherwise, return the cached response
        return cached_response.decode('utf-8')
    # return the wrapper function
    return wrapper

@cache_page
def get_page(url: str) -> str:
    """
    Get the HTML content of a URL.
    """
    return requests.get(url).text
