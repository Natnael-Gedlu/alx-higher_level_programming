#!/usr/bin/python3
"""
Defines a Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square.

        :param size: Size of the Square.
        :param x: X coordinate of the Square.
        :param y: Y coordinate of the Square.
        :param id: Unique identifier of the Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for size.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Update attributes of the Square instance based on arguments.

        Args:
            *args: Variable number of positional arguments.
            **kwargs: Variable number of keyword arguments.
        """
        if args:
            arg_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(arg_names):
                    setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return a dictionary representation of the Square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
