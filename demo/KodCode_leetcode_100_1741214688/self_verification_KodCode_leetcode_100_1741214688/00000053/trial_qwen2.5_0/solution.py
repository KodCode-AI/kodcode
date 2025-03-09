def find_smallest_path(grid, k):
    """
    Returns the lexicographically smallest path of length k from (0, 0) to (m-1, n-1).
    """
    m, n = len(grid), len(grid[0])
    
    def dfs(x, y, k, path):
        if k == 0 or x == m-1 and y == n-1:
            return [path]
        smallest_paths = []
        if x < m-1:
            smallest_paths += dfs(x+1, y, k-1, path + [grid[x+1][y]])
        if y < n-1:
            smallest_paths += dfs(x, y+1, k-1, path + [grid[x][y+1]])
        return sorted(smallest_paths, key=lambda p: int(''.join(map(str, p))))[:1]
    
    return dfs(0, 0, k, [grid[0][0]])[0]