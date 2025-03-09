def is_fibonacci(num: int) -> bool:
    """
    Checks if the given number is a Fibonacci number.
    
    A number is Fibonacci if one or both of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square.
    """
    def is_perfect_square(x: int) -> bool:
        s = int(x**0.5)
        return s*s == x
    
    return is_perfect_square(5*num**2 + 4) or is_perfect_square(5*num**2 - 4)