#!/usr/bin/python3
"""function that returns True if the
object is an instance of a class
that inherited (directly or indirectly)
from the specified class"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance
    """
    if type(obj) == a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
