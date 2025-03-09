def min_flips_to_connect(grid):
    """
    Returns the minimum number of 0s to flip to connect at least one landlocked area to the boundary.
    If it's impossible, returns -1.
    """
    m, n = len(grid), len(grid[0])
    
    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
            return
        grid[x][y] = 0  # Mark as visited by turning it to water
        # Explore all four directions
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
    
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if grid[i][j] == 1:
                visited = set()
                dfs(i, j)
                # Check all four boundaries to see if we can connect a landlocked area
                for k in range(n):
                    if grid[0][k] == 0 or grid[m - 1][k] == 0:
                        return 1
                    if (0, k) not in visited and grid[0][k] == 1:
                        return 2
                    if (m - 1, k) not in visited and grid[m - 1][k] == 1:
                        return 2
                for k in range(m):
                    if grid[k][0] == 0 or grid[k][n - 1] == 0:
                        return 1
                    if (k, 0) not in visited and grid[k][0] == 1:
                        return 2
                    if (k, n - 1) not in visited and grid[k][n - 1] == 1:
                        return 2
                return -1
    return -1