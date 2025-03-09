def longest_snake(grid):
    """
    Returns the length of the longest snake starting from the top-left corner
    and moving rightmost.
    """
    m, n = len(grid), len(grid[0])
    visited = set()
    max_snake_length = 0
    
    def explore(x, y, direction):
        nonlocal max_snake_length
        if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 0 or (x, y) in visited:
            return 0
        visited.add((x, y))
        max_snake_length = max(max_snake_length, 1 + explore(x + 1 * (direction[0] > 0 or direction[1] == 0), y + 1 * (direction[0] == 0 or direction[1] > 0), direction))
        visited.remove((x, y))
        return 1 + explore(x + direction[0], y + direction[1], direction)
    
    explore(0, 0, (1, 0))
    return max_snake_length