#!/usr/bin/python3
"""A function that defines an object attribute lookup."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
