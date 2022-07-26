#!/usr/bin/python3
"""Define a class called square"""


class Square:
    """The square class"""
    def __init__(self, __size=0):
        if type(__size) is not int:
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError ("size must be >= 0")
        else:
            self.__size = __size
