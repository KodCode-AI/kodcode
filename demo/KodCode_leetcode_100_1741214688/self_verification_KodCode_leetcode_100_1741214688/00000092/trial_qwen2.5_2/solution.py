from collections import deque

def shortest_border_path(grid):
    """
    Returns the shortest path from 'S' to any border land cell, or -1 if no such path exists.
    """
    if not grid or not grid[0]:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    
    start = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'W':
                grid[r][c] = '#'
    
    queue = deque([(start, 0)])
    visited.add(start)
    
    while queue:
        (r, c), steps = queue.popleft()
        if r in [0, rows-1] or c in [0, cols-1]:
            return steps
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), steps + 1))
                
    return -1