#!/usr/bin/python3
for num in range(0, 9):
    for i in range(num + 1, 10):
        if i == 8:
            print("{}{}".format(num, i))
        else:
            print("{}{}".format(num, i), end=", ")
