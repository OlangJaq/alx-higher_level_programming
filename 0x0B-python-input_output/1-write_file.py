#!/usr/bin/python3
"""
Module to write a file
"""

def write_file(filename="", text=""):
    """
    Function that writes a string
    args:
        filename(str): name of file.
        text (str): text to be written.
    returns the number of charaters written
    """
    with open("my_first_file.txt", mode="w", encoding="UTF-8") as file:
        return (file.write(text))
