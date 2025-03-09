def has_path_with_target(grid, target):
    """
    Determines if there exists a path from the top-left corner to the bottom-right corner
    such that the sum of the values along the path is exactly target.
    """
    m, n = len(grid), len(grid[0])
    dp = [[False] * n for _ in range(m)]
    dp[0][0] = grid[0][0] == target
    
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] and grid[i][0] == target - grid[i-1][0]
    
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] and grid[0][j] == target - grid[0][j-1]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = (dp[i-1][j] and grid[i][j] == target - grid[i-1][j]) or \
                       (dp[i][j-1] and grid[i][j] == target - grid[i][j-1])
    
    return dp[-1][-1]