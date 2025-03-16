def factorial(n: int) -> int | None:
    """
    Returns the factorial of n using recursion. If n is a negative integer, 
    the function returns None. For n=0 or n=1, the function returns 1.
    """
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)