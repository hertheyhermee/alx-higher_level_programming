#!/usr/bin/python3
"""Defines a function that checks class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj: Object to check.
        a_class: Class to match type of obj to.
    Returns:
        True if obj is exactly an instance of a_class.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
