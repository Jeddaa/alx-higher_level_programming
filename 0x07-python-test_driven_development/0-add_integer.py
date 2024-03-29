#!/usr/bin/python3
"""This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b)."""


def add_integer(a, b=98):
    """Returns a + b in integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
