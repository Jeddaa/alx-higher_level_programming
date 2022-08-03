#!/usr/bin/python3
"""a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "a+", encoding="utf-8") as file1:
        file2 = list(file1)
        for i in range(len(file2)):
            print(file2[i])
            if file2[i] == search_string:
                print(file1.write(new_string))
