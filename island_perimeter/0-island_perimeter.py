#!/usr/bin/python3
"""Create a function that returns the perimeter of an island."""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid."""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add one if the top side touches water or the grid border.
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                # Add one if the bottom side touches water or the grid border.
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

                # Add one if the left side touches water or the grid border.
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                # Add one if the right side touches water or the grid border.
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
