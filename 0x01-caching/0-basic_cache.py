#!/usr/bin/env python3
"""
    BasicCache class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic Cache class inheriting from BaseCaching
        No limit to cache items
    """
    def __init__(self):
        """ initializing """
        super().__init__()

    def put(self, key, item):
        """ Insert into cache
        Args:
            key (str): key of item
            item (str): item to insert

        Description: do nothing if either is None

        Return:
            No return
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve from cache """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data.get(key)
