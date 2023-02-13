#!/usr/bin/python3
"""Class that defines a rectangle"""""


class Rectangle:
    """This class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        p = self.__width * 2 + self.height * 2

        if self.__width == 0 or self.__height == 0:
            p = 0

        return p

    def __str__(self):
        w = self.__width
        h = self.__height
        print_rec = ""

        if w == 0 or h == 0:
            return ""

        for a in range(h):
            print_rec += "#" * w + "\n"

        if print_rec != 0:
            print_rec = print_rec[:-1]

        return print_rec
