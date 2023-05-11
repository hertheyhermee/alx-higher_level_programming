#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    reslut = 0
    for a in range(len(sys.argv) - 1):
        result = result + int(sys.argv[a + 1])
        print("{:d}".format(result))
