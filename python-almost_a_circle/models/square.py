#!/usr/bin/python3
"""Mudule: square.py
Unittest: tests/test_square.py"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """attributes of square"""

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return information"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, Value):
        """setter size"""
        self.width = Value
        self.height = Value

    def to_dictionary(self):
        """return format of dictionary"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        """update the values of rectangle instances"""
        if len(args) == 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])
        else:
            tupla = [
                "id",
                "size",
                "x",
                "y",
            ]
            for i in range(len(args)):
                setattr(self, tupla[i], args[i])
