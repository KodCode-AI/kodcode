def fibonacci(n):
    """
    Returns the nth Fibonacci number.
    
    The Fibonacci sequence is a series of numbers where the next number is found by adding up the two numbers before it.
    Starting with 0 and 1, the sequence goes 0, 1, 1, 2, 3, 5, 8, 13, and so forth.
    
    Args:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)