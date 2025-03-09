import math

def is_perfect_square(n):
    """
    Checks if a given number n is a perfect square.
    
    A perfect square is an integer that is the square of an integer.
    """
    if n < 0:
        return False
    root = math.isqrt(n)
    return n == root * root