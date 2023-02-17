#!/usr/bin/python3
"""
This function returns True if the object
is an instance of a class that inherited
(directly or indirectly) from the specified class,
otherwise False.
"""


def inherits_from(obj, a_class):
    """ inherit from a class
    """
    if type(obj) == a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
