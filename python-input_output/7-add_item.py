#!/usr/bin/python3
"""Script that adds all arguments to a Python list,
    and then save them to a file"""


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    json_data = load_from_json_file("add_item.json")
except FileNotFoundError:
    with open("add_item.json", "w") as f:
        f.write("[]")
    if not sys.argv[1]:
        exit(0)
    json_data = load_from_json_file("add_item.json")

for argv_data in sys.argv[1:]:
    json_data.append(argv_data)
save_to_json_file(json_data, "add_item.json")
