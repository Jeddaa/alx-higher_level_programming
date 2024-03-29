#!/usr/bin/python3
"""Define a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle"""
    def __init__(self, width, height):
        """intialize width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """define area"""
        return self.__width * self.__height

    def __str__(self):
        """define str"""
        rect = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return rect
