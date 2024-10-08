#!/usr/bin/python3
"""
Module that calculates the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A 2D list representing the island map.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found land
                # Check up (i - 1)
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check down (i + 1)
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left (j - 1)
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right (j + 1)
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
