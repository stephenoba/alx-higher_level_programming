#!/usr/bin/python3
# 10-best_score.py

def best_score(a_dictionary):
    """retruns a key with the largest integer"""
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    return None
