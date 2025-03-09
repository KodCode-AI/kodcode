def min_land_bridges(grid, k):
    """
    Returns the minimum number of land bridges needed to connect
    the leftmost and rightmost columns of the grid, or -1 if it's impossible.
    """
    m, n = len(grid), len(grid[0])
    left_to_right = [[False] * n for _ in range(m)]
    cnt_ones = 0
    
    # Create a bitmask for each row that indicates which columns have land (1) or water (0)
    row_bitmasks = [int(''.join(str(int(cell == 1)) for cell in row), 2) for row in grid]
    
    def dfs(r, mask):
        if mask == int('1' * n, 2):
            return 0
        if r == m - 1:
            return float('inf')
        if not (left_to_right[r] or (k and (mask & row_bitmasks[r]) == row_bitmasks[r])):
            return dfs(r + 1, mask)
        # Flip one 0 to 1
        if k:
            return 1 + min(dfs(r + 1, mask | (1 << j)) for j in range(n) if not (mask >> j) & 1)
        # No 0s to flip
        return float('inf')
    
    res = dfs(0, 0)
    return res if res != float('inf') else -1