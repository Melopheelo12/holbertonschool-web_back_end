#!/usr/bin/env python3
"""Complex types"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a list of integers and floats and returns sum """
    return float(sum(mxd_lst))
