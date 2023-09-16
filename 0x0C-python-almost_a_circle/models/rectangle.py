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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
            self.__y = value
