#!/usr/bin/python3
"""function that returns True if the
object is an instance of a class
that inherited (directly or indirectly)
from the specified class"""


def inherits_from(obj, a_class):
    """inheritance validation"""

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
