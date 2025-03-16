import math

def is_perfect_square(num: int) -> bool:
    if num < 0:
        return False
    s = math.isqrt(num)
    return s * s == num