#!/usr/bin/python3
"""
A method that calculates the fewest number of
operations needed to result in exactly n H characters
"""


def minOperations(n):
    """
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if n <= 1:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i

        for j in range(i - 1, 1, -1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
                break

    return dp[n]
