#!/usr/bin/python3
"""Returns True if the object is exactly an instance
    of the specified class,  otherwise False"""


def is_same_class(obj, a_class):
    """Instance verification"""

    return type(obj) is a_class
