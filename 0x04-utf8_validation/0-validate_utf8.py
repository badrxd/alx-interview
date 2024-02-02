#!/usr/bin/python3
'''UTF-8 Validation'''


def validUTF8(data):
    '''method that determines if a given data set represents a valid UTF-8 encoding'''
    ln = len(data)
    bytes = 0
    for i in range(ln):
        to_bin = data[i] & 255
        if bytes == 0:
            if to_bin >> 7 == 0:
                bytes = 0
                continue
            elif to_bin >> 5 == 6:
                bytes = 1
            elif to_bin >> 4 == 14:
                bytes = 2
            elif to_bin >> 3 == 30:
                bytes = 3
            else:
                return False
        else:
            if to_bin >> 6 != 2:
                return False
            else:
                bytes -= 1
    return True
