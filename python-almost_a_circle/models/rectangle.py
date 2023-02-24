#!/usr/bin/python3
"""
Mudule: rectangle.py
Unittest: tests/test_rectangle.py
"""

from models.base import Base


class Rectangle(Base):
    """Returns the width attributes"""

    def __init__(self, width, height, x=0, y=0, id=None,):
        self.staticfunc(width, "width")
        self.staticfunc(height, "height")
        self.staticfunc(x, "x")
        self.staticfunc(y, "y")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @staticmethod
    def staticfunc(value, name_met):
        """private Static method"""
        if type(value) != (int):
            raise TypeError(f"{name_met} must be an integer")
        if value <= 0 and name_met in ("width", "height"):
            raise ValueError(f"{name_met} must be > 0")
        if value < 0 and name_met in ("x", "y"):
            raise ValueError(f"{name_met} must be >= 0")

    def to_dictionary(self):
        """return a dictionary"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }

    def area(self):
        """Returns the area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """Prints a rectangle to stdout"""
        if self.__y > 0:
            for h in range(self.__y):
                print()
        for i in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            for c in range(self.__width):
                print("#", end="")
            print()

    @property
    def width(self):
        """Returns the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        self.staticfunc(value, "width")
        self.__width = value

    @property
    def height(self):
        """Returns the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        self.staticfunc(value, "height")
        self.__height = value

    @property
    def x(self):
        """Returns the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of x"""
        self.staticfunc(value, "x")
        self.__x = value

    @property
    def y(self):
        """Returns the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of y"""
        self.staticfunc(value, "y")
        self.__y = value

    def __str__(self):
        """Returns a string representation of a Rectangle"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Updates rectangle values"""
        if len(args) == 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])
        else:
            tupla = [
                "id",
                "width",
                "height",
                "x",
                "y"
            ]
            for i in range(len(args)):
                setattr(self, tupla[i], args[i])
