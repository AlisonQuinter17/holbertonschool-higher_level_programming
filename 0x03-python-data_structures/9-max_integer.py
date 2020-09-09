#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()
    if my_list != 0:
        return my_list[-1]
    else:
        return None
