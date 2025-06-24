#!/usr/bin/python3
"""This module is used to create a class"""


class Square:
    """Defines a class with private attributes"""
    def __init__(self, size=0):
        """Initializes size of the square"""
        self.__size = size
        
    @property
    def size(self):
        """Retrieves the size of square"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Sets the size of square if there is no exception"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """Returns the area of square"""
        return self.__size ** 2
