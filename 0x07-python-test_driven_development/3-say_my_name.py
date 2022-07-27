#!/usr/bin/python3
"""A function that prints 'My name is <first name> <last name>'"""


def say_my_name(first_name, last_name=""):
    """prints first name and last name if only they are strings"""
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    elif type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
