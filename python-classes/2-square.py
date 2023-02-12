#!/usr/bin/python3
"""Creating a Square class"""


class Square:
    """We are going to define a square"""

    def __init__(self, size=0):
        """The the data of the square"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
