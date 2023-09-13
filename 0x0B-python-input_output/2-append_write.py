#!/usr/bin/python3
"""
Defines a function that appends a string to a text file.
"""


def write_file(filename="", text=""):
    """
    function that returns the number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
