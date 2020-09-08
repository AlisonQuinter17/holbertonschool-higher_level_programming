#!/usr/bin/python3
def element_at(my_list, idx):
    for run in my_list:
        if idx < 0:
            return (None)
        if run == idx:
            return run + 1
    if idx > run - 1:
        return (None)
