def calculate_paths(n: int) -> int:
    """
    Returns the number of unique paths in an n x n grid.
    """
    # The number of unique paths in an n x n grid is given by the binomial coefficient C(2n, n)
    # which is (2n)! / (n! * n!)
    from math import comb

    return comb(2 * n, n)