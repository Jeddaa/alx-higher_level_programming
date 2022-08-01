#!/usr/bin/python3
"""Define a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        """initializing square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """defining string"""
        sq = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return sq
