def is_perfect_square(x):
    s = int(x ** 0.5)
    return s * s == x

def is_fibonacci_number(n):
    """
    Returns True if n is a Fibonacci number, False otherwise.
    """
    # A number is Fibonacci if one or both of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)