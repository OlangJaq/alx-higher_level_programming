#!/usr/bin/python3
"""
Create object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file"
    Args:
        filename(str): file from which object if to be loaded.
    """
    with open(filename, mode="r", encoding="utf-8") as json_file:
        my_obj = json.load(json_file)
        return my_obj
