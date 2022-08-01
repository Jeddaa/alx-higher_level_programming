#!/usr/bin/python3
"""Define a class: BaseGeometry"""


class BaseGeometry():
    """ Basegeometry class """
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if not isinstance (value, int):
            raise TypeError(("{} must be an integer").format(name))
        elif value <= 0:
            raise ValueError(("{} must be greater than 0").format(name))
