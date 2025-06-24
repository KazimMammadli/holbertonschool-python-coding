#!usr/bin/python3
"""This model is used to create Square class"""


class Square:
    """It defines a class with a private instance attribute"""
    def __init__(self, size=0):
        """Initializes the attribute and raise exception if needed"""
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
