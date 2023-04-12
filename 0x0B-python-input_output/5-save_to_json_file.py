#!/usr/bin/python3
"""
Save Object to a file using JSON
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.
    Args:
        my_obj (object): object to be serialized.
        filename (str): name of file where string is stored.

    """
    with open(filename, mode='w', encoding='UTF-8') as json_file:
        return (json.dump(my_obj, json_file))
