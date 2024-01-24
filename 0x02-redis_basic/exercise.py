#!/usr/bin/env python3
"""
Module for the Cache class
"""

import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps

def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and
    outputs for a particular function
    """
    inputs = f"{method.__qualname__}:inputs"
    outputs = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function for the decorator
        """
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result

    return wrapper

class Cache:
    """
    Cache class for redis client
    """

    def __init__(self):
        """
        Initialize the Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float]:
        """
        Get the value from Redis by key
        """
        result = self._redis.get(key)
        if fn:
            return fn(result)
        return result

    def get_str(self, key: str) -> str:
        """
        Get the value from Redis by key and convert it to a string
        """
        result = self._redis.get(key)
        return result.decode("utf-8")

    def get_int(self, key: str) -> int:
        """
        Get the value from Redis by key and convert it to an integer
        """
        result = self._redis.get(key)
        return int(result)

def replay(method: Callable):
    """
    Display the history of calls of a particular function
    """
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"
    count = method.__self__._redis.llen(inputs)
    print(f"{method.__qualname__} was called {count} times:")
    for inp, out in zip(method.__self__._redis.lrange(inputs, 0, -1), method.__self__._redis.lrange(outputs, 0, -1)):
        print(f"{method.__qualname__}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")
