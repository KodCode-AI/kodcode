def has_valid_path(grid, target):
    """
    Determine if there exists a path from the top-left corner to the bottom-right corner
    such that the sum of the values along the path is exactly `target`.

    :param grid: List[List[int]] - A 2D list of integers representing the grid.
    :param target: int - The target sum.
    :return: bool - True if such a path exists, False otherwise.
    """
    m, n = len(grid), len(grid[0])
    memo = {}

    def dfs(x, y, current_sum):
        if x == m or y == n or current_sum > target:
            return False
        if x == m - 1 and y == n - 1:
            return current_sum == target
        if (x, y, current_sum) in memo:
            return memo[(x, y, current_sum)]

        memo[(x, y, current_sum)] = dfs(x + 1, y, current_sum + grid[x][y]) or dfs(x, y + 1, current_sum + grid[x][y])
        return memo[(x, y, current_sum)]

    return dfs(0, 0, grid[0][0])