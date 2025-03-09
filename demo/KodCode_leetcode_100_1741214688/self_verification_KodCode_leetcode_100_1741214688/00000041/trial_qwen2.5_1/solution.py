from collections import deque

def min_land_bridges(grid, k):
    """
    Returns the minimum number of land bridges needed to connect the leftmost and rightmost columns
    of the grid, or -1 if it is impossible to do so with the given k 0s.
    """
    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def is_bridged():
        visited = [[False] * n for _ in range(m)]
        queue = deque()
        
        # Mark all land cells in the leftmost column as visited
        for i in range(m):
            if grid[i][0] == 1:
                queue.append((i, 0))
                visited[i][0] = True
                
        while queue:
            x, y = queue.popleft()
            if y == n - 1:
                return True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                    elif k > 0:
                        k -= 1
                        queue.append((nx, ny))
                        visited[nx][ny] = True
        return False
    
    # Check if the grid is already bridged
    if is_bridged():
        return 0
    
    # Count the number of 0s needed to bridge the grid
    for i in range(m):
        if is_bridged():
            return 1
    
    return -1 if k == 0 else 1