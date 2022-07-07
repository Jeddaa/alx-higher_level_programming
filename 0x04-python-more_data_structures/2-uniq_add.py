#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    total = 0
    for i in range(len(my_list)):
        if my_list[i] not in unique:
            unique.append(i)
            total += my_list[i]
    return total
