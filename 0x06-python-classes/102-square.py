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
        Initialize a square with a size.

        :param size: The size of the square's sides (default is 0).
        :type size: int
        :raises TypeError: If size is not a number (float or integer).
        :raises ValueError: If size is less than 0.
        """
        self.size = size

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
        :raises TypeError: If size is not a number (float or integer).
        :raises ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        :return: The area of the square.
        :rtype: int
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare two Square instances for equality based on area.

        :param other: The other Square instance to compare.
        :type other: Square
        :return: True if the areas are equal, False otherwise.
        :rtype: bool
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare two Square instances for inequality based on area.

        :param other: The other Square instance to compare.
        :type other: Square
        :return: True if the areas are not equal, False otherwise.
        :rtype: bool
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compare two Square instances for less than based on area.

        :param other: The other Square instance to compare.
        :type other: Square
        :return: True if the area of self is less than the area of
        other, False otherwise.
        :rtype: bool
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare two Square instances for less than or equal to based on area.

        :param other: The other Square instance to compare.
        :type other: Square
        :return: True if the area of self is less than or equal
        to the area of other, False otherwise.
        :rtype: bool
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compare two Square instances for greater than based on area.

        :param other: The other Square instance to compare.
        :type other: Square
        :return: True if the area of self is greater than the
        area of other, False otherwise.
        :rtype: bool
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare two Square instances for greater than
        or equal to based on area.

        :param other: The other Square instance to compare.
        :type other: Square
        :return: True if the area of self is greater than
        or equal to the area of other, False otherwise.
        :rtype: bool
        """
        return self.area() >= other.area()
