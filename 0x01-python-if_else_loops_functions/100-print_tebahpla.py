#!/usr/bin/python3
for char in reversed(range(97, 123)):
    if char % 2 == 1:
        char = char - 32
    print(chr(char), end="")
