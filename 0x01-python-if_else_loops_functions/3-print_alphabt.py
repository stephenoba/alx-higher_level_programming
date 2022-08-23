#!/usr/bin/python3

"""
prints the ASCII alphabet except 'e' and 'q',
in lowercase, not followed by a new line
"""
for char in range(97, 123):
    if chr(char) is not 'e' and chr(char) is not 'q':
        print(f"{chr(char)}", end="")
