#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for run in my_list[::-1]:
        print("{}".format(run, end=""))
