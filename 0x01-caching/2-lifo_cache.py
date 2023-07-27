#!/usr/bin/env python3
""" LIFOCache module
"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache defines a caching system using LIFO eviction policy
    """
    def __init__(self):
        """ Initialize LIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache using LIFO eviction policy
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Get the last key (LIFO) to discard and remove it from the cache
                last_key = next(reversed(self.cache_data))
                del self.cache_data[last_key]
                print("DISCARD:", last_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key from the cache using LIFO eviction policy
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
