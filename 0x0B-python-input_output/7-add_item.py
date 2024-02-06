#!/usr/bin/python3
'''task 7 module'''


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arglist = list(sys.argv[1:])

try:
    old_data = load_from_json_file('add_item.json')
except Exception:
    old_data = []

old_data.extend(arglist)
save_to_json_file(old_data, 'add_item.json')
