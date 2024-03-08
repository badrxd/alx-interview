#!/usr/bin/python3
""" Island perim solution"""


def island_perim(grid):
    """ island perim function """
    row = len(grid),
    col = len(grid[0])
    perim = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                perim += 4
                if i > 0 and grid[i-1][j] == 1:
                    perim -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perim -= 2
    return perim
