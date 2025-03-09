def num_paths_memo(m, n, memo={}):
    """
    Returns the number of unique paths from the top-left corner to the bottom-right corner of an M x N grid.
    Can only move down or right.
    Uses memoization for optimization.
    """
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 1 or n == 1:
        return 1
    memo[(m, n)] = num_paths_memo(m - 1, n, memo) + num_paths_memo(m, n - 1, memo)
    return memo[(m, n)]