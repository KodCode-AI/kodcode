def fibonacci(n: int) -> int:
    """ Returns the nth Fibonacci number using recursion. """
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)