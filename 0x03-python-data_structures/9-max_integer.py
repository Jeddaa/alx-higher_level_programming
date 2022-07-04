#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return(None)
    else:
        maxy = my_list[0]
        for i in my_list:
            if i > maxy:
                maxy = i
        return maxy
