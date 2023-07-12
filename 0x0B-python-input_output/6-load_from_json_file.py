#!/usr/bin/python3
"""import json"""
import json


"""function that creates an Object from a “JSON file”"""


def load_from_json_file(filename):
    """creating a JSON file"""
    with open(filename) as f:
        return (json.load(f))
