#!/usr/bin/python3
"""Defines text file-reading function."""


def read_file(filename=""):
    """Print contents of UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
