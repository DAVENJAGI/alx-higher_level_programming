#!/usr/bin/python3
"""import json"""
import json


"""function that writes an Object to text file using a JSON representation"""


def save_to_json_file(my_obj, filename):
    """returned value"""
    with open(filename, "w") as f:
        return (json.dump(my_obj, f))
