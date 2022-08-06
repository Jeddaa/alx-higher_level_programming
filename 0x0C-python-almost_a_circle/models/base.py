#!/usr/bin/python3
"""Define a class Base"""
import json


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

    """returns the JSON representation of list_dictionaries"""
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
