#!/usr/bin/python3
"""Define a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """ the class Rectangle that inherits from class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        """Call to super function to have
        access to all attributes/methods"""
        super().__init__(id)
    
    """retrieving the width"""
    @property
    def width(self):
        return self.__width

    """setting the width"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value
    
    """retrieving x"""
    @property
    def x(self):
        return self.__x

    """setting x"""
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    """retrieving y"""
    @property
    def y(self):
        return self.__y

    """setting the width"""
    @width.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value