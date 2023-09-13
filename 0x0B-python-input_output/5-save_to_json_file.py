#!/usr/bin/python3
"""
Defines a function that write an object to JSON file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that saves to JSON file.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
