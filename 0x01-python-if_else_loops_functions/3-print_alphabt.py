#!/usr/bin/python3

"""
prints the ASCII alphabet except 'e' and 'q',
in lowercase, not followed by a new line
"""
for char in range(97, 123):
    if (char == 101) or (char == 113):
        continue
    print(f"{chr(char)}", end="")
