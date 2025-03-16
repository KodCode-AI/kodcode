import math

def is_perfect_square(num: int) -> bool:
    if num < 0:
        return False
    sqrt_num = math.isqrt(num)
    return sqrt_num * sqrt_num == num