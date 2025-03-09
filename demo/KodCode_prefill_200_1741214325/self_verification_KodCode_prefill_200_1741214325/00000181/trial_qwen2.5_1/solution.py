def fibonacci_up_to_n(n):
    """
    Returns a list containing Fibonacci numbers up to the given limit 'n'.
    
    Parameters:
    n (int): The upper limit for generating Fibonacci numbers.
    
    Returns:
    list: A list of Fibonacci numbers up to 'n'.
    """
    if n < 0:
        return []
    fib_sequence = [0, 1]
    next_fib = fib_sequence[-1] + fib_sequence[-2]
    while next_fib <= n:
        fib_sequence.append(next_fib)
        next_fib = fib_sequence[-1] + fib_sequence[-2]
    return fib_sequence