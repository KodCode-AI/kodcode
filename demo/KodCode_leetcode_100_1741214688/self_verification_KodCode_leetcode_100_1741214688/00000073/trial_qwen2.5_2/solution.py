def explore_snake(grid, x, y, visited):
    """
    Recursively explore the snake and mark visited cells.
    """
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    length = 1  # Starting from the current cell
    max_length = 0

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1 and (new_x, new_y) not in visited:
            visited.add((new_x, new_y))
            length += explore_snake(grid, new_x, new_y, visited)
            max_length = max(max_length, length)
            visited.remove((new_x, new_y))

    return max_length

def longest_snake(grid):
    """
    Returns the length of the longest snake starting from (0, 0) and moving rightmost.
    """
    if grid[0][0] == 0:
        return 0  # Starting point is water, no snake to explore
    visited = {(0, 0)}
    return explore_snake(grid, 0, 0, visited)