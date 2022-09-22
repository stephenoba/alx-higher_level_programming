#!/usr/bin/python3
# 5-text_indentation.py
# Stephen Oba <obastepheno@gmail.com>
"""module provides a function to indent a text"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: `.`,
    `?` and `:`

    Args:
        text (str): Text to indent

    Raises:
        TypeError: if text is not a string

    Return:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ['.', '?', ':']:
            if text[c] in ['.', '?', ':']:
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
