#!/usr/bin/python3
def safe_print_integer(value):
    ans = " "
    try:
        int(value)
        ans = True
        print("{:d}".format(value))
    except (ValueError, TypeError):
        ans = False
    return ans
