#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    position = new_list.index(search, 0)
    new_list[position] = replace
    return new_list
