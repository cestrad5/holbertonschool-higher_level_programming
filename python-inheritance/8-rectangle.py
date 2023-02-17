#!/usr/bin/python3
""" This function is used to generate BaseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is a subclass of BaseGeometry
    """

    def __init__(self, width: int, height: int):
        """
        Initializes a Rectangle object with a specified width and height.
        The constructor uses the integer_validator method from the BaseGeometry
        class to validate the width and height arguments.
        Parameters:
        - width: An integer representing the width of the rectangle.
        - height: An integer representing the height of the rectangle.
        Example usage:
        >>> r = Rectangle(3, 4)
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width
