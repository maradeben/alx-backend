#!/usr/bin/env python3
"""
    LRUCache module
    Implementing a caching system using the
    Least Recently Used (LRU) algo
"""
from base_caching import BaseCaching


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
        self.data = []
        # data is a list of lists [key, value, age]
        self.age_bit = 0  # age bit of items

        super().__init__()

    def put(self, key, item):
        """ insert into cache using LRU """
        all_keys = [item[0] for item in self.data]
        # confirm not none
        if key is not None and item is not None:
            # if a hit
            if key in all_keys:
                for i in range(len(self.data)):
                    # if key match is found, update
                    if self.data[i][0] == key:
                        self.data[i][1] = item
                        self.data[i][2] = self.age_bit
                        self.age_bit += 1
                        break
            else:  # it's a miss
                if len(self.data) >= LRUCache.MAX_ITEMS:  # cache is full
                    # delete youngest item
                    ages = [item[2] for item in self.data]
                    to_del = self.data[ages.index(min(ages))]
                    print("DISCARD: {}".format(to_del[0]))
                    del self.data[ages.index(min(ages))]
                # add the new data
                self.data.append([key, item, self.age_bit])
                self.age_bit += 1

        # reload self.cache_data
        self.cache_data = {}
        for k, v, _ in self.data:
            self.cache_data[k] = v
        print(self.data)

    def get(self, key):
        """ retrieve item """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data.get(key)
