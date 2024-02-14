#!/usr/bin/python3
'''N Queens'''
from sys import argv, exit


def check():
    pass


def search(level, potison):
    matrix_size = level
    default_value = 0
    board = [[default_value] * matrix_size for _ in range(matrix_size)]


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
    solutions = search(int(argv[1]), 0)


if __name__ == "__main__":
    nqueens(argv)
