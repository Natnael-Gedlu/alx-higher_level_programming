#!/usr/bin/python3
"""
Defines a Base model class.
"""
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        :param list_dictionaries: A list of dictionaries.
        :return: A JSON string representing the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        :param cls: The class itself.
        :param list_objs: A list of instances that inherit from Base.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dicts)

        with open(filename, 'w') as file:
            file.write(json_str)
