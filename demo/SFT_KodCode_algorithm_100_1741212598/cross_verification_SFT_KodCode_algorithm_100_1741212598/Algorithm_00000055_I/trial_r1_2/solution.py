import math

def calculate_paths(n: int) -> int:
    return math.comb(2 * n, n)