#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    for run in my_list:
        i = i + 1
        if idx < 0:
            return (None)
        if run == idx:
            return run + 1
    if idx > i - 1:
        return (None)
