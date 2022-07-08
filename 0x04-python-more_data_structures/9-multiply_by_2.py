#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        diction = {}
        new_diction = {}
        for key, value in a_dictionary.items():
            new_value = value * 2
            diction = {key: new_value}
            new_diction.update(dicto)
        return new_diction
