#!/usr/bin/python3
'''N Queens'''
from sys import argv, exit


def nqueens(argv):

    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        assert int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if int(argv[1]) < 4:
        print('N must be at least 4')
        exit(1)
    return []

if __name__ == "__main__":
    nqueens(argv)
