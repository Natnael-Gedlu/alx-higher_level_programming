#!/usr/bin/python3
"""
Defines a function that returns JSON format to object.
"""
import json


def from_json_string(my_str):
    """
    function returns the object representation of JSON string.
    """
    return json.loads(my_str)
