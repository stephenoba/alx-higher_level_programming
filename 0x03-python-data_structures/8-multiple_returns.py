#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """get length of sentence and first character"""
    first_char = None
    length = len(sentence)
    if length > 0:
        first_char = sentence[0]
    return length, first_char
