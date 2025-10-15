"""
DAT5501 – Unit Testing activity.

This module intentionally stays tiny so the focus is on professional practice:
- clear requirements via docstrings and tests
- robust input validation
- TDD cycle (red → green → refactor)
"""

from typing import Union

Number = Union[int, float]

def increment(x: Number, /) -> Number:
    if not isinstance(x, (int, float)):
        raise TypeError("x must be an int or float")
    if isinstance(x, float) and (x != x or x in (float("inf"), float("-inf"))):
        raise ValueError("x must be a finite number")
    return x + 1

