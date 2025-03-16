import math

def is_fibonacci(n):
    if not isinstance(n, int):
        if isinstance(n, float) and n.is_integer():
            n = int(n)
        else:
            return False
    if n < 0:
        return False
    def is_perfect_square(x):
        if x < 0:
            return False
        s = int(math.sqrt(x))
        return s * s == x
    a = 5 * n * n + 4
    b = 5 * n * n - 4
    return is_perfect_square(a) or is_perfect_square(b)