#!/usr/bin/env python3
""" givon page and page size, return start and stop index """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ calculate and return start/stop indices """
    stop = page * page_size
    start = stop - page_size

    return (start, stop)
