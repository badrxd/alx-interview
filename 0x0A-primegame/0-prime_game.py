#!/usr/bin/python3
"""
define is winner function
"""


def Primes(n):
    """ list of primes"""
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(player, nums):
    """
        define winner function
    """
    if player is None or nums is None or player == 0 or nums == []:
        return None
    mariaCount = 0
    benCount = 0
    for i in range(player):
        prime = Primes(nums[i])
        if len(prime) % 2 == 0:
            benCount += 1
        else:
            mariaCount += 1
    if benCount > mariaCount:
        return 'Ben'
    elif mariaCount > benCount:
        return 'Maria'
    return None
