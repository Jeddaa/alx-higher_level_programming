#!/usr/bin/python3
def no_c(my_string):
    copy = [strng for strng in my_string if strng != 'c' and strng != 'C']
    return ("".join(copy))
