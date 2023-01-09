#!/usr/bin/python3
"""checks if an object is an instance of a class"""

def is_same_class(obj, a_class):
    """is same class
    Args:
        obj: object input
        a_class: class input
    Returns:
        True if the object is exactly an instance of the specified
        class else False
    """
    if type(obj) == a_class:
        return True
    else:
        return False