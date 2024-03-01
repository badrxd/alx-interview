#!/usr/bin/python3
"""Making the change"""


def makeChange(coins, the_total):
    """making the change"""
    if the_total <= 0:
        return 0

    dp = [float('inf')] * (the_total + 1)
    dp[0] = 0

    for i in range(1, the_total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[the_total] if dp[the_total] != float('inf') else -1


print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))
