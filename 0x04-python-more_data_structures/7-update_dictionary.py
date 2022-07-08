#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        a_dictionary.update({key: value})
        for key, value in sorted(a_dictionary.items()):
            print("{}: {}".format(key, value))
