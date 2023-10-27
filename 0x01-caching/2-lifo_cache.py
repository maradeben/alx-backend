#!/usr/bin/env python3
"""
    LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ FIFOCache module, inherits from BaseCaching

    Class Attributes:
        MAX_ITEMS: maximum cache items acceptable
            remove last inserted to make space for new if full

    Methods:
        put - insert into cache, but mind MAX_ITEMS
        get - retrieve from cache
    """

    def __init__(self):
        """ initialize by inheriting from parent """
        super().__init__()

    def put(self, key, item):
        """ insert into cache
        No. of cache items must not exceed max size
        if full, remove last inserted to make space for new
        """

        if key is not None and item is not None:
            if len(self.cache_data) >= LIFOCache.MAX_ITEMS and \
                    key not in self.cache_data.keys():
                to_del = list(self.cache_data.keys())[-1]
                print("DISCARD: {}".format(to_del))
                del self.cache_data[to_del]
            self.cache_data[key] = item

    def get(self, key):
        """ retrieve from cache """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data.get(key)
