#!/usr/bin/python3
"""the logic that determines if all the boxes can be opened."""
def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened.
    boxes:list of the boxes
    """
    box = set()
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            num = boxes[i][j]
            if num != i and num not in box and num != 0:
                box.add(num)
    return True if len(boxes)-1 == len(box) else False
