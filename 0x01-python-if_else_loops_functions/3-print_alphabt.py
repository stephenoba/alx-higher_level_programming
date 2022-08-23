#!/usr/bin/python3
for char in range(97, 123):
    if chr(char) is not 'e' and chr(char) is not 'q':
        print("{}".format(chr(char)), end="")
