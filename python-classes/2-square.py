#!/usr/bin/python3
"""This module is used to create a class"""


class Square:
    """This class is used to find the area of square
    with the help of given parameter"""
    def __init__(self, size=0):
        """Raises exceptions depending of the type and value errors"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
