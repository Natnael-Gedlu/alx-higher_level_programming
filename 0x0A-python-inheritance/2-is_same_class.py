#!/usr/bin/python3
"""
Defines a class that checks object is an instance.
"""


def is_same_class(obj, a_class):
    """
    Determine if an object belongs to a specific class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class,
              False otherwise.

    """
    if type(obj) == a_class:
        return True
    return False
