#!/usr/bin/python3
"""
Defines a script that adds all arguments to a Python list
and then save them to a file.
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

list_args = []

try:
    list_args = load_from_json_file("add_item.json")
except FileNotFoundError:
    list_args = []

for arg in args:
    list_args.append(arg)

save_to_json_file(list_args, "add_item.json")
