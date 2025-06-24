#!/usr/bin/python3
"""This model is used to create Square class"""


class Square:
    """It defines a class with a private instance attribute"""
    def __init__(self, size=0):
        """Initializes the attribute and raise exception if needed"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
