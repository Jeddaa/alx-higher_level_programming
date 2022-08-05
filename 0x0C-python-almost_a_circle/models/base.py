#!/usr/bin/python3
"""Define a class Base"""


class Base:
    """the Base class"""
    __nb_objects = 0
    """the class constructor"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
