#!/usr/bin/python3
"""A function that prints a square with character '#'"""


def print_square(size):
    """prints a square with '#'"""
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif type(size) not in [int]:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for i in range(size):
                print("#", end='')
            print()
