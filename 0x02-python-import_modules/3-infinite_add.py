#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    new = 0
    for i in range(1, len(argv)):
        new += argv[i]
    print('{:d}'.format(new))
