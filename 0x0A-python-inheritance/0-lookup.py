#!/usr/bin/python3
"""
Contains definition of funtion lookup
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj(any): objects whose attributes and methords are returned
    """

    attrs = dir(obj)
    methods = [attr for attr in attrs if callable(getattr(obj, attr))]
    return attrs + methods
