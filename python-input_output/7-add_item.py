#!/usr/bin/python3
import sys
import json
from os import path


def save_to_json_file(my_obj, filename):
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    if path.exists(filename):
        with open(filename, mode="r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return []

filename = "add_item.json"
if not path.exists(filename):
    save_to_json_file([], filename)

my_list = load_from_json_file(filename)

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
