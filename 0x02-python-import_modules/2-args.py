#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    argc = len(args) - 1
    if argc == 1:
        print("{} argument:".format(argc))
    elif argc == 0:
        print("{} arguments.".format(argc))
    else:
        print("{} arguments:".format(argc))

    for i in range(1, len(args)):
        print("{}: {}".format(i, args[i]))
