#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_list = []
    for key, val in a_dictionary.items():
        if val == value:
            del_list.append(key)
    for elem in del_list:
        del a_dictionary[elem]
    return a_dictionary
