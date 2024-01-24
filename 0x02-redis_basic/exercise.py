#!/usr/bin/env python3
"""
Module for the Cache class
"""

import redis
import uuid
from typing import Union, Optional, Callable

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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
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
