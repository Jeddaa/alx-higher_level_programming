#!/usr/bin/python3
"""a function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """read and print text from a file"""
    with open(filename, encoding="utf-8") as file1:
        print(file1.read().end="")
