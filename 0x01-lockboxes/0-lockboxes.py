#!/usr/bin/python3
def canUnlockAll(boxes):
    box = set()
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            num = boxes[i][j]
            if num != i and num not in box and num != 0:
                box.add(num)
    return True if len(boxes)-1 == len(box) else False
