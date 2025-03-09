def max_snake_length(grid):
    """
    Finds the maximum length of a snake starting from [0, 0] and moving to the rightmost boundary.
    """
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    max_len = 0
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Right, Down, Up, Left
    
    def dfs(x, y, parent_dir):
        nonlocal max_len
        if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 0:
            return 0
        if parent_dir != directions[0]:  # Ensure only move right
            return 0
        steps = 1
        grid[x][y] = 0  # Mark as visited
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (dx, dy) == parent_dir:
                continue
            steps = max(steps, dfs(nx, ny, (dx, dy)) + 1)
        max_len = max(max_len, steps)
        return steps
    
    dfs(0, 0, (0, 0))
    return max_len