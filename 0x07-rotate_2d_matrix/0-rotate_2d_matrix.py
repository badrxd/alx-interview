#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """methode that take 2d matrix and retate it 90°"""
    row = len(matrix[0])
    colum = len(matrix)
    matrix_2 = []

    for i in range(row):
        matrix_2.append([])
        for y in range(colum):
            matrix_2[i].append(matrix[y][i])

    matrix = matrix_2
    matrix_2 = None

    for i in range(row):
        for y in range(int(colum/2)):
            tmp = matrix[i][y]
            matrix[i][y] = matrix[i][colum-y-1]
            matrix[i][colum-y-1] = tmp
