#!/usr/bin/python3
"""Define a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square"""
    def __init__(self, size):
        """initializing square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
