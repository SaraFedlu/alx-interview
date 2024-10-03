#!/usr/bin/python3
"""
Make Change - Dynamic Programming Solution
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of integers representing coin denominations.
        total (int): The total amount to be formed using the fewest coins.

    Returns:
        int: The fewest number of coins needed,
        or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order to prioritize larger coins
    coins.sort(reverse=True)

    # Initialize dp array with 'infinity' for all values except dp[0]
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # For each coin, update dp values
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
            # Early exit if we've already computed a solution for `total`
            if dp[total] != float('inf'):
                return dp[total]

    # If dp[total] is still 'infinity', return -1 (total can't be met)
    return dp[total] if dp[total] != float('inf') else -1
