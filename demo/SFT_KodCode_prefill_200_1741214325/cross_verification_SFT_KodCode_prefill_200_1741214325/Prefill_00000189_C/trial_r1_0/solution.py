import math

def is_fibonacci_number(n: int) -> bool:
    """Returns True if n is a Fibonacci number, False otherwise."""
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)
    
def is_perfect_square(x: int) -> bool:
    if x < 0:
        return False
    s = math.isqrt(x)
    return s * s == x