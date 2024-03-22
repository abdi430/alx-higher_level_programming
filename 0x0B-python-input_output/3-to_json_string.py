#!/usr/bin/python3
""" string to josn"""
def write_file(filename="", text=""):
    """function that writes a string to a text file and return the number
    of characters written"""

    with open(filename, 'w') as f:
        return f.write(text)
