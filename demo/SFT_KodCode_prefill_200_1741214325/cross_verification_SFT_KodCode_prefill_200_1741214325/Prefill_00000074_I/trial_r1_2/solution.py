import math

def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    s = math.isqrt(n)
    return s * s == n