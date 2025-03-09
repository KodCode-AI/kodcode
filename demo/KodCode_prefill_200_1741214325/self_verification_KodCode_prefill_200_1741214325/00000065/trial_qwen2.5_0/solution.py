def fibonacci(n):
    """
    Returns the nth Fibonacci number.
    
    The Fibonacci sequence is defined by the following:
    F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b