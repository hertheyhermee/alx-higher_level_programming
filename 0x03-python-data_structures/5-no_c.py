#!/usr/bin/python3
def no_c(my_string):
    chars_to_remove = ["c", "C"]
    new_string = "".join([char for char in my_string if char not in chars_to_remove])
    return new_string
