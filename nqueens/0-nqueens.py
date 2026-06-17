#!/usr/bin/python3
"""N Queens solver.

This module solves the N Queens puzzle using backtracking.
Only the sys module is imported, as required by the project.
"""

import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


queens = []


def is_safe(row, col, queens):
    """Check if a queen can be placed at the given row and column.

    Args:
        row: The current row.
        col: The current column.
        queens: The list of already placed queens.

    Returns:
        True if the position is safe, otherwise False.
    """
    # Compare the new queen with every queen already placed.
    for r, c in queens:
        # Same column or same diagonal means the position is not safe.
        if c == col or abs(r - row) == abs(c - col):
            return False

    return True


def solve(row):
    """Place queens row by row using backtracking.

    Args:
        row: The current row where we try to place a queen.
    """
    # If row == N, all queens are placed, so we found a solution.
    if row == N:
        print(queens)
        return

    # Try every column in the current row.
    for col in range(N):
        if is_safe(row, col, queens):
            # Choose: place a queen.
            queens.append([row, col])

            # Explore: try to place the next queen.
            solve(row + 1)

            # Unchoose: remove the queen and try another position.
            queens.pop()


solve(0)
