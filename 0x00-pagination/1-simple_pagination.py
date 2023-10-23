#!/usr/bin/env python3
""" Server module """
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ calculate and return start/stop indices """
    stop = page * page_size
    start = stop - page_size

    return (start, stop)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get page specified """
        assert type(page) == int and type(page_size) == int 
         assert page > 0 and page_size > 0 
         start, end = index_range(page, page_size) 
         data = self.dataset() 
         if start > len(data): 
             return [] 
         return data[start:end]
