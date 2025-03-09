import math

def is_perfect_square(n):
    """
    Check if a given number is a perfect square.
    """
    if n < 0:
        return False
    root = math.isqrt(n)
    return n == root * root