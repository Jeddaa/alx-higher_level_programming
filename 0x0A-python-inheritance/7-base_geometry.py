#!/usr/bin/python3
"""Define a class: BaseGeometry"""


class BaseGeometry():
    """ Basegeometry class """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the integers"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
