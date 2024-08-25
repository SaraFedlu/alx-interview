#!/usr/bin/python3
"""
Minimum Operations
"""

def minOperations(n: int) -> int:
    """Calculates the fewest number of operations needed to achieve n 'H' characters."""
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2

    # Factorizing n by dividing by the smallest factors
    while n > 1:
        # If the current divisor is a factor, reduce n and add the divisor to the operations count
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations
