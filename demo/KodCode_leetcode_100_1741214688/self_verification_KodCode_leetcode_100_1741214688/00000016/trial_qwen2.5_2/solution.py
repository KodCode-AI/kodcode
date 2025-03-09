def maxNumberOfIslands(grid):
    """
    Returns the maximum number of islands that can be formed.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (
            not (0 <= r < rows and 0 <= c < cols)
            or grid[r][c] == "0"
            or (r, c) in visited
        ):
            return 0
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        return 1

    return sum(dfs(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "1")