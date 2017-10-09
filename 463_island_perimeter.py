"""
https://leetcode.com/problems/island-perimeter/description/
463. Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        Steps:
            Say grid has m rows (length of grid) and n columns (length of each list inside the grid)
            - Loop through all cells within the grid
                - For cells == 1, find the count of 1s surrounding it by passing the cell index for left, right, up, down
                - Then do appropriate perimieter calculation
        """
        # Height = m, number of rows (Iterate x on this)
        height = len(grid)
        # Length = n, number of columns (Iterate y on this)
        length = len(grid[0])
        # Function inputs index of a unit and outputs value, if exists
        def surround_island(x,y):
            # For out-of-index cells, return 0
            if x < 0 or x > height - 1 or y < 0 or y > length - 1:
                return 0
            else:
                # Otherwise return the value
                return grid[x][y]
        # perimeter to calculate perimeter
        perimeter = 0
        x = 0
        while x < height:
            y = 0
            while y < length:
                # Only check for cells that are equal to 1
                if grid[x][y] == 1:
                    # Check its neighbors
                    counter = surround_island(x + 1, y) + surround_island(x, y + 1) + surround_island(x - 1, y) + surround_island(x, y - 1)
                    # Perimeter added by this cell
                    perimeter = perimeter + (4 - counter)
                y = y + 1
            x = x + 1
        return perimeter
