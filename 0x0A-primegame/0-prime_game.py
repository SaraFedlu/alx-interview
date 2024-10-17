#!/usr/bin/python3
"""
Prime Game - Determine the winner after multiple rounds of prime number games
"""


def sieve_of_eratosthenes(max_num):
    """
    Returns a list where index i is True if i is a prime number, False ow.
    Uses the Sieve of Eratosthenes to compute primes up to max_num.
    """
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False
    return primes


def count_prime_moves(n, primes):
    """
    Count how many moves can be made for a given n.
    This function returns the number of possible moves in a game of size n.
    """
    numbers = [True] * (n + 1)
    moves = 0

    for i in range(2, n + 1):
        if primes[i] and numbers[i]:
            moves += 1
            for j in range(i, n + 1, i):
                numbers[j] = False
    return moves


def isWinner(x, nums):
    """
    Determines the winner of x rounds of the prime game.

    Args:
        x (int): The number of rounds.
        nums: A list of integers representing the 'n' values for each round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben").
             Returns None if there is a tie.
    """
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        moves = count_prime_moves(n, primes)
        if moves % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
