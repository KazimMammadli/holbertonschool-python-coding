#!/usr/bin/python3
"""This module creates a class"""


class Square:
    def __init__(self, size=0):
        """Initializes the value of size"""
        self.__size = size

    @property
    def size(self):
        """Returns the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints square with #, if size is zero, prints blank line"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(self.__size * "#")
