#!/usr/bin/python3
"""Minimum operations module."""


def minOperations(n):
    """Return the minimum operations needed to get n H characters."""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        # If factor divides n, it is part of the optimal decomposition.
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            # Otherwise, try the next possible factor.
            factor += 1

    return operations
