#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """the rectangle class"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    """area of the rectangle"""
    def area(self):
        return self.__height * self.__width

    """perimeter of the rectangle"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    """printing the rectangle using '#'"""
    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        rec = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return rec

    """string representation of the rectangle """
    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """print 'Bye rectangle...' when an instance of rectangle is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
