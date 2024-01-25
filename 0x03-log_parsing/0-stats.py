#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


def print_fn(status, File_size):
    """ print function"""

    print("File size: {}".format(File_size))
    for key in sorted(status):
        val = status[key]
        if val > 0:
            print("{} {}".format(key, val))


File_size = 0
lines = 0
status = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

try:
    for line in sys.stdin:
        lines += 1
        data = line.split()
        try:
            key = int(data[-2])
            status[key] += 1
        except Exception as err:
            pass

        try:
            file_size = int(data[-1])
            File_size += file_size
        except Exception as err:
            pass

        if lines % 10 == 0:
            print_fn(status, File_size)
finally:
    print_fn(status, File_size)
