#!/usr/bin/python3
"""function that returns True if the
object is an instance of a class
that inherited (directly or indirectly)
from the specified class"""


def inherits_from(obj, a_class):
    """issubclass is used for compare two class"""

    if isinstance(obj, a_class) & issubclass(a_class, obj.__class__) is False:
        return True
    return False
