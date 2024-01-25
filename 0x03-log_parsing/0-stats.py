#!/usr/bin/python3
"""reads stdin line by line and computes metrics """

from sys import stdin


status_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
count = 0


def print_fn():
    """function to print all"""
    print("File size:", total_file_size)
    for key, value in status_code.items():
        if value:
            print("{}: {}".format(key, value))


try:
    for line in stdin:
        count += 1
        line = line.split()
        try:
            file_size = int(line[-1])
            total_file_size += file_size
        except (IndexError, ValueError, TypeError):
            continue
        try:
            code = int(line[-2])
            if code in status_code.keys():
                status_code[code] += 1
        except (IndexError, ValueError, TypeError):
            continue
        if count == 10:
            print_fn()
            count = 0
    print_fn()
except KeyboardInterrupt:
    print_fn()
