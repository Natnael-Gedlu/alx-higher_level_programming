#!/usr/bin/python3
"""
Defines a function that adds attributes to objects.
"""


def add_attribute(obj, att, value):
    """
    Add a new attribute to an object.

    Args:
        obj (object): The object to which the attribute will be added.
        att (str): The name of the attribute to add.
        value (any): The value to assign to the new attribute.

    Raises:
        TypeError: If the object does not support adding new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
