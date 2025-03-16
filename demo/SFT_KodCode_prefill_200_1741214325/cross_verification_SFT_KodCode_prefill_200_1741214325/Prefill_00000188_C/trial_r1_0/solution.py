def fibonacci(n: int) -> int:
    """ Returns the nth Fibonacci number using recursion.
    Handles negative n by returning 0 and follows the sequence starting with 0, 1, 1, 2, etc.
    """
    if n < 0:
        return 0
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)