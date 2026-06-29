#!/usr/bin/python3
"""Module for rotating a 2D matrix."""


def rotate_2d_matrix(matrix):
    """Rotate a square 2D matrix 90 degrees clockwise in-place."""
    n = len(matrix)

    # Transpose the matrix by swapping rows and columns.
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the clockwise rotation.
    for row in matrix:
        row.reverse()
