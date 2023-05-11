#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv) - 1
    if l == 0:
        print("0 arguments.")
    elif l == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(l))
    for y in range(l):
        print("{}: {}".format(y + 1, sys.argv[y + 1]))
