def min_landlock_flips(grid):
    """
    Returns the minimum number of 0s that need to be flipped
    to make at least one landlocked area non-landlocked.
    If it's impossible, returns -1.
    """
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()

    def is_landlock(i, j):
        if (i, j) in visited:
            return False
        visited.add((i, j))
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 1:
                return False
            if is_landlock(x, y):
                return True
        return True

    def count_zeros(i, j):
        if (i, j) in visited:
            return 0
        visited.add((i, j))
        count = int(grid[i][j] == 0)
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n:
                count += count_zeros(x, y)
        return count

    flips = float('inf')
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 or (i, j) in visited:
                continue
            if is_landlock(i, j):
                min_val = count_zeros(i, j)
                flips = min(flips, min_val)

    return flips if flips != float('inf') else -1