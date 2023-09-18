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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize instances to CSV format and save them to a file.

        :param cls: The class itself.
        :param list_objs: A list of instances that inherit from Base.
        """
        filename = cls.__name__ + ".csv"

        with open(filename, 'w') as file:
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    file.write(f"{obj.id},{obj.width},{obj.height},{obj.x},{obj.y}\n")
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    file.write(f"{obj.id},{obj.size},{obj.x},{obj.y}\n")

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize instances from a CSV file and return a list of instances.

        :param cls: The class itself.
        :return: A list of instances.
        """
        filename = cls.__name__ + ".csv"
        instances = []

        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    values = line.strip().split(',')
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(values[1]), int(values[2]), int(values[3]), int(values[4]), int(values[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(int(values[1]), int(values[2]), int(values[3]), int(values[0]))
                    instances.append(obj)
        except FileNotFoundError:
            pass

        return instances