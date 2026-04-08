#!/usr/bin/env python3
"""Complex types"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float multiplier and returns a function"""
    def multiplier_func(n: float) -> float:
        return n * multiplier

    return multiplier_func