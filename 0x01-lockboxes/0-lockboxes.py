#!/usr/bin/python3
"""the logic that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened.
    boxes:list of the boxes
    """
    box = set()
    max = len(boxes)
    for i in range(max):
        for j in range(len(boxes[i])):
            num = boxes[i][j]
            if num != i and num not in box and num != 0 and num < max:
                box.add(num)

    return True if max-1 == len(box) else False
