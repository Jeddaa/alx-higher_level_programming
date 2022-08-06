#!/usr/bin/python3
"""Define a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the class Square that inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Call to super function to have
        access to all attributes/methods"""
        super().__init__(size, size, x, y, id=None)
        """validation of attribute: size"""
        self.size = size
    """retrieving the size using the width"""
    @property
    def size(self):
        return self.__width

    """setting the width"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
    