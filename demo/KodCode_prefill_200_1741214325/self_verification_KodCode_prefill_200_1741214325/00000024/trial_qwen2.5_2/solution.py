def count_paths(m, n, memo={}):
    """
    Returns the number of unique paths from the top-left corner to the bottom-right corner
    of an M x N grid. Movement is restricted to only down or right.
    """
    key = (m, n)
    if key in memo:
        return memo[key]
    if m == 1 or n == 1:
        return 1  # Base case: if either dimension is 1, there's only one way to reach the end
    memo[key] = count_paths(m - 1, n, memo) + count_paths(m, n - 1, memo)
    return memo[key]