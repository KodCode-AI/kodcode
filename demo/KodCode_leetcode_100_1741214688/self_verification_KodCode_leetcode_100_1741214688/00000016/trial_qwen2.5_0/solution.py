def maxNumberOfIslands(grid):
    """
    Returns the maximum number of islands that can be formed by changing the
    0's to 1's in the grid.
    """
    def fill(grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 0:
            return
        grid[i][j] = 2  # Mark as visited
        fill(grid, i + 1, j)
        fill(grid, i - 1, j)
        fill(grid, i, j + 1)
        fill(grid, i, j - 1)

    max_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                fill(grid, i, j)
                max_islands += 1

    return max_islands