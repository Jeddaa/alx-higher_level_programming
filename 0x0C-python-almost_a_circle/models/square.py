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
