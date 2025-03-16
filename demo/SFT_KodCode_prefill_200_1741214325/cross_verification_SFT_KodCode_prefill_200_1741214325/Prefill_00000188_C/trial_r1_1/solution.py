def fibonacci(n: int) -> int:
    """ Returns the nth Fibonacci number using recursion.
    >>> fibonacci(0) 
    0
    >>> fibonacci(1) 
    1
    >>> fibonacci(2) 
    1
    >>> fibonacci(5) 
    5
    >>> fibonacci(9) 
    34
    >>> fibonacci(-5) 
    0
    """
    if n < 0:
        return 0
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)