def has_path_with_target(grid, target):
    """
    Determines if there exists a path from the top-left corner to the bottom-right corner
    such that the sum of the values along the path is exactly `target`.
    """
    m, n = len(grid), len(grid[0])
    return dfs(grid, target, 0, 0, m, n)

def dfs(grid, target, i, j, m, n):
    if i == m or j == n or grid[i][j] == -1:
        return False
    if i == m - 1 and j == n - 1 and grid[i][j] == target:
        return True
    temp = grid[i][j]
    grid[i][j] = -1
    found = dfs(grid, target - temp, i + 1, j, m, n) or dfs(grid, target - temp, i, j + 1, m, n)
    grid[i][j] = temp
    return found