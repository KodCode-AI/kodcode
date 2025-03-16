import math

def count_paths(m: int, n: int) -> int:
    return math.comb(m + n - 2, m - 1)