#!/usr/bin/python3
"""
Defines a function that returns object to JSON format.
"""
import json


def to_json_string(my_obj):
    """
    function returns the JSON representation of an object.
    """
    return json.dumps(my_obj)
