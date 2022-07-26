#!/usr/bin/python3
"""Define a class called square"""


class Square:
    """create a square instance"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """retrieve size"""
    @property
    def size(self):
        return self.__size

    """set size attribute"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """retrieve positon"""
    @property
    def position(self):
        return self.__position

    """set postion attribute"""
    @position.setter
    def position(self, value):
        if type(value) != tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """calculate area"""
    def area(self):
        return self.__size * self.__size

    """print square"""
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for line in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print('#', end="")
                print("")
