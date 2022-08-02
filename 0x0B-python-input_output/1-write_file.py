#!/usr/bin/python3
"""a function that writes a string to a text file
(UTF8) and returns the number of characters written"""


def write_file(filename="", text=""):
    """writes a string to a file"""
    with open(filename, "r", encoding="utf-8") as file1:
        file1.write(text)
