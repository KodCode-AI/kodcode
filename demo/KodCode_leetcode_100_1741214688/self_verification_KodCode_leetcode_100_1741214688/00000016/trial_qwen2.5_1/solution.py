def max_islands(grid):
    """
    Returns the maximum number of islands that can be formed in the grid.
    """
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    
    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0 or visited[x][y]:
            return
        visited[x][y] = True
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
    
    max_islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                max_islands += 1
    return max_islands