import math

def is_fibonacci(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    a = 5 * n * n + 4
    b = 5 * n * n - 4
    s_a = math.isqrt(a)
    s_b = math.isqrt(b)
    return (s_a * s_a == a) or (s_b * s_b == b)