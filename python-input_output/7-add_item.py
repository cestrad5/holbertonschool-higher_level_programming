#!/usr/bin/python3
"""script that adds all arguments to a Python list, and then save them to a file"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(filename=""):
    """write a file"""

    try:
        file_json = load_from_json_file(filename)
    except Exception:
        file_json = []

    for i in sys.argv[1:]:
        file_json.append(i)
    save_to_json_file(file_json, filename)


filename = "add_item.json"
add_item(filename)
