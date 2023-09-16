#!/usr/bin/python3
"""
Defines a Base model class.
"""


class Base:
    """
    Base class to be used as basic template for
    other classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        :param id: An integer representing a unique identifier.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
