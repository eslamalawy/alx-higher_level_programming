#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list_copy = my_list.copy()
    my_list_copy[idx] = element
    return my_list_copy
