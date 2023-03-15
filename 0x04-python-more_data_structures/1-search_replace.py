#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_lst = []
    for item in my_lst:
        if item == search:
            new_lst.append(replace)
        else:
            new_lst.append(item)
    return new_lst
