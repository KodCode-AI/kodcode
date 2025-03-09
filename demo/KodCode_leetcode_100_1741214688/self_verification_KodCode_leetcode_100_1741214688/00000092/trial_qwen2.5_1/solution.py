from collections import deque

def shortest_path_to_border(grid):
    """
    Finds the shortest path from the start position to any border cell that is also land.
    :param grid: List[List[str]], a 2D grid representing the map.
    :return: int, the number of steps in the shortest path or -1 if no path exists.
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = None
    visited = set()
    
    # Find the start position
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
                break
        if start:
            break
    
    if not start:
        return -1
    
    queue = deque([(start, 0)])
    visited.add(start)
    
    while queue:
        (r, c), dist = queue.popleft()
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                grid[nr][nc] == 'L' and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))
                
    return -1