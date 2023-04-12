#!/usr/bin/python3
"""
Function that appends a file
"""


def append_write(filename="", text=""):
    """append_write appends string at the end of a text file.

    Args:
        filename (str): name of file.
            text (str): text to be appended to the file.
        Returns: number of characters written.
    """
    with open(filename, mode="a", encoding="UTF-8") as file:
        return (file.write(text))
