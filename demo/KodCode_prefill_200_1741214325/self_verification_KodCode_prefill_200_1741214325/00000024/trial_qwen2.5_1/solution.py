import functools

def count_paths(m, n):
    """
    Returns the number of paths from the top-left corner to the bottom-right corner of an M x N grid.
    Movement is restricted to down and right.
    """
    @functools.lru_cache(maxsize=None)
    def dp(r, c):
        if r == 0 or c == 0:
            return 1
        return dp(r - 1, c) + dp(r, c - 1)
    
    return dp(m - 1, n - 1)