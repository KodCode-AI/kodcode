def fibonacci(n):
    """
    Returns the nth Fibonacci number and a list of the first n Fibonacci numbers.
    """
    if n <= 0:
        return 0, []
    elif n == 1:
        return 1, [0]
    elif n == 2:
        return 1, [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    return fib_sequence[-1], fib_sequence