#!/usr/bin/python3
"""Define a class Base"""
import json


class Base:
    """the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """the class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        objs = []
        if list_objs is not None:
            for obj in list_objs:
                objs.append(cls.to_dictionary(obj))
        file1 = cls.__name__ + ".json"
        with open(file1, "w") as f:
            f.write(cls.to_json_string(objs))
