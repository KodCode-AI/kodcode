def fibonacci(n):
    """
    Returns the nth Fibonacci number.
    
    The Fibonacci sequence is a series of numbers where each number is the sum
    of the two preceding ones, usually starting with 0 and 1. That is,
    F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.
    
    Parameters:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The nth Fibonacci number.
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