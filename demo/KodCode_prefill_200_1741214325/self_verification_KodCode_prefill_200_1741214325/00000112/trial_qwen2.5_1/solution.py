def generate_fibonacci(n):
    """
    Generates the Fibonacci sequence up to a given number n and returns a list of the Fibonacci numbers less than or equal to n.
    """
    if n < 0:
        return []
    
    fib_sequence = [0]
    a, b = 0, 1
    while b <= n:
        fib_sequence.append(b)
        a, b = b, a + b
    return fib_sequence