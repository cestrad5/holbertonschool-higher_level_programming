#!/usr/bin/python3
"""
Function that prints a square with the character #.
Prototype: def print_square(size):
size is the size length of the square.
"""


def print_square(size):
    """
    size must be an integer, otherwise raise a TypeError exception.
    """

    if size == "" or size == " " or size is None:
        raise TypeError("size must be an integer")

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        print(size * "#")
