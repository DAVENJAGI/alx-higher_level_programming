#!/usr/bin/python3
"""Function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file
    after each line containing a specific string"""
    txt = ""
    with open(filename) as r:
        for line in r:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
