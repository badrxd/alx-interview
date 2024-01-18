#!/usr/bin/python3
'''i used Prime Factorization to resolve this problem'''


def minOperations(n):
    ''' calculate fewest number of operations needed and return it'''
    nOperations = 0
    start = 2

    while n > 1:
        if n % start == 0:
            n = n/start
            nOperations += start
        else:
            start += 1
    return nOperations
