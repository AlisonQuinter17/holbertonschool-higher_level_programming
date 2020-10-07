#!/usr/bin/python3
"""Module for read_lines function."""


def read_lines(filename="", nb_lines=0):
    """This function reads n lines of a text file."""
    with open(filename, "r", encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")

        else:
            i = f.readlines()[0: nb_lines]

            for x in i:
                print(x, end="")
