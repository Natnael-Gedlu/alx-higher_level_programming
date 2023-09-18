#!/usr/bin/python3
"""
Defines a Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle.
        :param width: Width of the Rectangle.
        :param height: Height of the Rectangle.
        :param x: X coordinate of the Rectangle.
        :param y: Y coordinate of the Rectangle.
        :param id: Unique identifier of the Rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for x.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        :return: Area of the Rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the Rectangle instance with the character #.
        """
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Return a string representation of the Rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        """
        Update attributes of the Rectangle based on arguments.

        Args:
            *args: Variable number of arguments in the following order:
                1st argument: id attribute
                2nd argument: width attribute
                3rd argument: height attribute
                4th argument: x attribute
                5th argument: y attribute
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
