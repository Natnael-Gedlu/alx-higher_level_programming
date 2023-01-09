#!/usr/bin/python3
"""
Define a funciton to find the instance of the object
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is instance of a class that inherited from,
     the specified class, or False otherwise
    """
    return isinstance(obj, a_class)