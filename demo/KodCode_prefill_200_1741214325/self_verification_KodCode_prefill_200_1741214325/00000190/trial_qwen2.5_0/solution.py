import math

def is_perfect_square(n):
    """
    Returns True if n is a perfect square, False otherwise.
    """
    if n < 0:
        return False
    root = math.isqrt(n)
    return n == root * root