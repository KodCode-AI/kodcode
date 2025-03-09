def fibonacci(n):
    """
    Returns the nth Fibonacci number.
    
    The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, starting with 0, and 1.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b