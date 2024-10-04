#!/usr/bin/python3
"""
Make Change - Optimized using BFS
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total

    Args:
        coins (list): A list of integers representing coin denominations.
        total (int): The total amount to be formed using the fewest coins.

    Returns:
        int: The fewest number of coins needed, or -1
    """
    if total <= 0:
        return 0

    # Use BFS to search for the fewest number of coins
    queue = [(0, 0)]  # (current_total, number_of_coins)
    visited = set()  # To avoid re-processing the same total

    # Sort coins to prioritize smaller ones
    coins.sort(reverse=True)

    while queue:
        current_total, num_coins = queue.pop(0)

        # Try all coins and explore new totals
        for coin in coins:
            new_total = current_total + coin

            # If we've exactly met the total, return the number of coins
            if new_total == total:
                return num_coins + 1

            # If the new total is less than the desired total
            if new_total < total and new_total not in visited:
                visited.add(new_total)
                queue.append((new_total, num_coins + 1))

    # If we exit the loop, it means we couldn't find a combination
    return -1
