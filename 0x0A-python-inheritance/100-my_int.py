#!/usr/bin/python3
"""Define a class MyInt that inherits from int"""


class MyInt(int):
    """class MyInt"""
    def __init__(self, no):
        """initialization of the integer"""
        self.no = no
    def __eq__(self, value):
        """ to return true if both are not equal"""
        return self.no != value

    def __ne__(self, value):
        """ to return true if both are not equal"""
        return self.no == value
