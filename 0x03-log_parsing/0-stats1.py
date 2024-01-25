#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys
# import re


def print_fn(status, File_size):
    """ print function"""

    print("File size: {}".format(File_size))
    for key in sorted(status):
        val = status[key]
        if val > 0:
            print("{} {}".format(key, val))


# ptr = (
#     r'^\d+\.\d+\.\d+\.\d+ - \[.*\] '
#     r'"GET \/projects\/\d+ HTTP\/\d.\d" '
#     r'\d{3} \d+$'
# )

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
        # match = re.match(ptr, line)
        data = line.split()

        # if match is not None:
        #     status[int(data[-2])] += 1

        try:
            status[int(data[-2])] += 1
        except Exception:
            pass

        try:
            File_size += int(data[-1])
        except Exception:
            pass

        if lines % 10 == 0:
            print_fn(status, File_size)
finally:
    print_fn(status, File_size)
