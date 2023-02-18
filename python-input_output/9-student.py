#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student CONSTRUCTOR"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method Returns: [type]: dict"""
        return self.__dict__
