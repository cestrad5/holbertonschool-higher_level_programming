#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”:"""


import json


def load_from_json_file(filename):
    """Read and json.load for created an object"""

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
