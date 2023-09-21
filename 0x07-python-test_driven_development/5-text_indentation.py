#!/usr/bin/python3
"""
    Function to print a new line
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    print(text, end="\n")
