#!/usr/bin/python3

"""A Lockboxes algorithm"""


def canUnlockAll(boxes):
    """A function  that determines if all the boxes can be opened."""
    for i in range(1, len(boxes)):
        others = boxes[:i] + boxes[i + 1:]
        for j in range(len(others)):
            for k in range(len(others[j])):
                if boxes[j][k] == i and i == j:
                    return True
            return False;
