#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """the rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """retrieve the width"""
    @property
    def width(self):
        return self.__width

    """setting the width"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """retrieving the height"""
    @property
    def height(self):
        return self.__height

    """setting the height"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
