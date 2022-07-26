#!/usr/bin/python3
"""a function that adds two integers"""


def add_integer(a, b=98):
    """Returns a + b in integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return a+b
