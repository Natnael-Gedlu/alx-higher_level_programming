#!/usr/bin/python3
"""
Define a class Square.
"""


class Square:
    """
    This class defines a square.
    """

    def __init__(self, size=0):
        """
        Initialize a square with an optional size.

        :param size: The size of the square's sides (default is 0).
        :type size: int
        :raises TypeError: If size is not an integer.
        :raises ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        :return: The area of the square.
        :rtype: int
        """
        return self.__size ** 2
