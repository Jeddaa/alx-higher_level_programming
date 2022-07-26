#!/usr/bin/python3
"""Define a class called square"""


class Square:
    """The square class"""
    def __init__(self, size=0):
        self.__size = size
    """retrieving the property"""
    @property
    def size(self):
        return self.__size
    """setting the property"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size
