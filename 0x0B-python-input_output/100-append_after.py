#!/usr/bin/python3
"""
Defines a text insertion to a file function.
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a new string after a specific search string in a text file.

    Parameters:
        filename (str): The name of the text file to add on.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert after the `search_string` if found.

    """
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as new:
        new.write(text)
