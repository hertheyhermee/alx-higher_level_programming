#!/usr/bin/python3
def no_c(my_string):
    chars = ["c", "C"]
    new_string = "".join([char for char in my_string if char not in chars])
    return new_string
