import math

def is_perfect_square(n):
    if n < 0:
        return False
    sqrt_n = math.sqrt(n)
    int_sqrt = int(sqrt_n)
    return int_sqrt * int_sqrt == n