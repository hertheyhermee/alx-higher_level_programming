#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_add = ()
    first_tuple = tuple_a + (0, 0)
    sec_tuple = tuple_b + (0, 0)
    tuple_add = first_tuple[0] + sec_tuple[0], first_tuple[1] + sec_tuple[1]
