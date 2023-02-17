#!/usr/bin/python3
"""This module have a class that inherits from BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, define size"""

    def __init__(self, size):
        """define size
        with super().__init__ define a square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
