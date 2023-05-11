#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv) - 1
    print("{} arguement".format(l), end="")
    if l == 0:
        print("s.")
    elif l == 1:
        print(":")
        print("{}: {}".format(l, sys.argv[l]))
    else:
        if l > 1:
            print("s", end="")
            print(":")
            for m in range(1, l + 1):
                print("{}: {}".format(m, sys.argv[m]))
