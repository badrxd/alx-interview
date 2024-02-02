#!/usr/bin/python3
'''UTF-8 Validation'''


def validUTF8(data):
    '''method that determines if a given data set
    represents a valid UTF-8 encoding
    '''
    ln = len(data)
    _bytes = 0
    if data is None:
        return
    for i in range(ln):
        to_bin = data[i] & 255
        if _bytes == 0:
            if to_bin >> 7 == 0:
                _bytes = 0
                continue
            elif to_bin >> 5 == 6:
                _bytes = 1
            elif to_bin >> 4 == 14:
                _bytes = 2
            elif to_bin >> 3 == 30:
                _bytes = 3
            else:
                return False
        else:
            if to_bin >> 6 != 2:
                return False
            else:
                _bytes -= 1
        if ln - 1 == i and _bytes > 0:
            return False
    return True
