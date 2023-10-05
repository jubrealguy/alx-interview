#!/usr/bin/python3

"""
A lockBoxes Program
"""


def canUnlockAll(boxes):
    """
    A method that determines if all the boxes can be opened.
    """
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            if boxes[i][j] == i:
                return True
    return False
