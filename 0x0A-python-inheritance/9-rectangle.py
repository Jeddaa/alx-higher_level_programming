#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Define a class"""


class Rectangle(BaseGeometry):
    """class rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {}/{}".format((self.__class__.__name__, self.__width, self.__height))
