#!/usr/bin/python3
"""
Module for read file methords.
"""

def read_file(filename=""):
    """
    Reads text file and prints to STDOUT
    """
    with open(filename, mode='r', encoding='UTF-8') as file:
        for line in file:
            print(line, end='')
