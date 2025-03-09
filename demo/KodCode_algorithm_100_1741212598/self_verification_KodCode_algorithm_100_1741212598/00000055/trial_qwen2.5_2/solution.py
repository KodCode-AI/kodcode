def calculate_paths(n: int) -> int:
    """
    Returns the number of unique paths in an n x n grid.
    """
    from math import comb
    return comb(2 * n, n)