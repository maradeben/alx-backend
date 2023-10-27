#!/usr/bin/env python3
"""
    LRUCache module
    Implementing a caching system using the
    Least Recently Used (LRU) algo
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache, inheriting from BaseCaching
    Class Attributes:
        MAX_ITEMS(int): acceptable by the cache

    Methods:
        put: insert into cache,
            discard least recently used if full
        get: retrieve a cache item
    """

    def __init__(self):
        """ initialize with the parent """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ insert into cache using LRU """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ retrieve item """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data.get(key)
