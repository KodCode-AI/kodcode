from collections import deque

def shortest_land_distance(grid):
    """
    Returns the shortest path from the start position to any border cell that is also land.
    If no such path exists, returns -1.
    """
    if not grid or not grid[0]:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    start_row, start_col = -1, -1
    
    # Find the start position
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start_row, start_col = i, j
                break
        if start_row != -1:
            break
    
    if start_row == -1:
        return -1
    
    # Perform BFS
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start_row, start_col, 0)])
    visited = set([(start_row, start_col)])
    
    while queue:
        row, col, steps = queue.popleft()
        
        if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
            if grid[row][col] == 'L':  # Check if it's a land cell on the border
                return steps
            continue
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 'L' and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, steps + 1))
    
    return -1