#!/usr/bin/python3
"""Define a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the class Square that inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Call to super function to have
        access to all attributes/methods"""
        super().__init__(size, size, x, y, id=None)
        """validation of attribute: size"""
        self.size = size
    """retrieving the size using the width"""
    @property
    def size(self):
        return self.width

    """setting the size"""
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}\
- {self.size}"

    """assigning arguments to each attributes using args and kwargs"""
    def update(self, *args, **kwargs):
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.size = value
                elif key == 2:
                    self.x = value
                elif key == 3:
                    self.y = value
            return self.__str__
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "id":
                    self.id = value
            return self.__str__
    
    """returns dictionary representation of square"""
    def to_dictionary(self):
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
