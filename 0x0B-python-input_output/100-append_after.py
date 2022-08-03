#!/usr/bin/python3
"""a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """appends a line of text after a specific string"""
    with open(filename, "r+", encoding="utf-8") as file1:
        new_str = ""
        for i in file1:
            new_str += i
            if search_string in i:
                new_str += new_string
        file1.seek(0)
        file1.write(new_str)
