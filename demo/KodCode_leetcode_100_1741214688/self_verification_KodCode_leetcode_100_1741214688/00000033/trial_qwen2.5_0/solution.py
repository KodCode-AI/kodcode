def min_flips(grid):
    """
    Returns the minimum number of flips required to make at least one landlocked area non-landlocked.
    If it's impossible, returns -1.
    """
    m, n = len(grid), len(grid[0])
    
    # Helper function to perform a flood fill
    def flood_fill(x, y, prev_value):
        if 0 <= x < m and 0 <= y < n and grid[x][y] == prev_value:
            grid[x][y] = 2  # Mark as visited
            flood_fill(x + 1, y, prev_value)
            flood_fill(x - 1, y, prev_value)
            flood_fill(x, y + 1, prev_value)
            flood_fill(x, y - 1, prev_value)
    
    def is_landlocked():
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 1 and all(grid[x][y] != 0 for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))):
                    return (i, j)
        return None
    
    flips = 0
    landlocked = is_landlocked()
    
    while landlocked:
        x, y = landlocked
        flood_fill(x, y, 0)
        grid[x][y] = 1
        flips += 1
        landlocked = is_landlocked()
    
    # Check if all land is connected to the boundary
    def is_connected():
        visited = set()
        
        def dfs(x, y):
            if (x, y) in visited:
                return
            visited.add((x, y))
            if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                return True
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] == 1:
                    if dfs(x + dx, y + dy):
                        return True
            return False
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 1 and (i, j) not in visited:
                    if not dfs(i, j):
                        return -1
        return flips
    
    return is_connected()