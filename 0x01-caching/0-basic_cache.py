#!/usr/bin/python3
"""
Module 0-basic_cache
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    Overrides put() and get()
    from parent
    """

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # If cache is full, remove the oldest item
                oldest_key = next(iter(self.cache_data))
                del self.cache_data[oldest_key]
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        return self.cache_data.get(key)
