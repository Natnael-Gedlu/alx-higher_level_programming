#!/usr/bin/python3
"""
Defines a Base model class.
"""
import json
import turtle
import csv

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

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.penup()
            turt.goto(rect.x, rect.y)
            turt.pendown()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.penup()
            turt.goto(sq.x, sq.y)
            turt.pendown()
            for _ in range(2):
                turt.forward(sq.size)
                turt.left(90)
                turt.forward(sq.size)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
