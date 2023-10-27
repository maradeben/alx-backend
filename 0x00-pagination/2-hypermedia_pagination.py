#!/usr/bin/env python3
""" Simple pagination
"""

import csv
from typing import List, Tuple, Dict
import math


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
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
        """Retrieves a page of data.
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ get page hyperparameters """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        data = self.get_page(page, page_size)
        prev_page = None if page is 1 else page - 1
        start, end = index_range(page, page_size)
        next_page = page + 1 if len(self.__dataset) > end + 1 else None
        # if there's still something after the 'end', then there's a next page
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_size = page_size if start < len(self.__dataset) else 0

        return ({
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
            })


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple containing a start and end index.
    """
    return ((page - 1) * page_size, page * page_size)
