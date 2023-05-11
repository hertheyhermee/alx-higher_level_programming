#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        total = add(a, b)
        for j in range(4, 6):
            total = add(total, j)
            return (total)
    else:
        return (sub(a, b)
