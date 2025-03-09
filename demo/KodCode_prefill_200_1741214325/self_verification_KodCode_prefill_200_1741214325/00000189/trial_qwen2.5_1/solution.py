def is_fibonacci(n):
    """
    Returns True if n is a Fibonacci number, False otherwise.
    """
    # A number is a Fibonacci only if one or both of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
    import math
    
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x
    
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)