#!/usr/bin/python3
"""
Defines a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    A custom integer class that changes the behavior of equality operators.
    """
    def __eq__(self, value):
        """
        Check if the instance is not equal to the given value.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Check if the instance is equal to the given value.
        """
        return self.real == value
