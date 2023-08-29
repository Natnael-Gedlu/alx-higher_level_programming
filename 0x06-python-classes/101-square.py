#!/usr/bin/python3
"""
Define a class Square.
"""


class Square:
    """
    This class defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square with an optional size and position.

        :param size: The size of the square's sides (default is 0).
        :type size: int
        :param position: The position of the square (default is (0, 0)).
        :type position: tuple of two positive integers
        :raises TypeError: If size is not an integer, or if position is not a tuple of two positive integers.
        :raises ValueError: If size is less than 0, or if position values are not positive.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        :return: The size of the square.
        :rtype: int
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        :param value: The size value to set.
        :type value: int
        :raises TypeError: If size is not an integer.
        :raises ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        :return: The position of the square.
        :rtype: tuple of two positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        :param value: The position value to set.
        :type value: tuple of two positive integers
        :raises TypeError: If position is not a tuple or its values are not positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        :return: The area of the square.
        :rtype: int
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using '#' characters.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)

    def __str__(self):
        """
        Return a string representation of the square.

        :return: A string representation of the square.
        :rtype: str
        """
        result = ""
        if self.__size == 0:
            result += '\n'
            return result

        for _ in range(self.__position[1]):
            result += '\n'

        for _ in range(self.__size):
            result += ' ' * self.__position[0] + '#' * self.__size + '\n'

        return result[:-1]
