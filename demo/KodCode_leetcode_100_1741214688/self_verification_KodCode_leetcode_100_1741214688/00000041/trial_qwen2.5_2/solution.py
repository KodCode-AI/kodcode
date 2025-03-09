def min_land_bridges(grid, k):
    """
    Returns the minimum number of land bridges needed to connect the leftmost
    and rightmost columns of the grid, or -1 if it's impossible with the given k.
    """
    m, n = len(grid), len(grid[0])
    queue = []
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited = [[False] * n for _ in range(m)]
    
    # Enqueue all land cells in the leftmost column.
    for i in range(m):
        if grid[i][0] == 1:
            queue.append((i, 0))
            visited[i][0] = True
    
    # Perform BFS to find connected components.
    while queue:
        x, y = queue.pop(0)
        if y == n - 1:
            # If current cell is in the rightmost column, return the number of 0s flipped.
            return 0 if k >= 0 else -1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if grid[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                elif k > 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    k -= 1
    
    # Check if rightmost column is reachable.
    if any(grid[i][n-1] == 1 for i in range(m)):
        return 1
    return -1