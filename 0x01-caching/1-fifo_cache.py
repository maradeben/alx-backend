#!/usr/bin/env python3
"""
    FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache module, inherits from BaseCaching

    Class Attributes:
        MAX_ITEMS: maximum cache items acceptable

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
        """

        if key is not None and item is not None:
            if len(self.cache_data) >= FIFOCache.MAX_ITEMS and \
                    key not in self.cache_data.keys():
                to_del = list(self.cache_data.keys())[0]
                print("DISCARD: {}".format(to_del))
                del self.cache_data[to_del]
            self.cache_data[key] = item

    def get(self, key):
        """ retrieve from cache """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data.get(key)
