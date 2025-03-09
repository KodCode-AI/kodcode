def generate_fibonacci(n):
    """
    Generate a Fibonacci sequence up to the number n.
    
    Parameters:
    n (int): The upper limit for the Fibonacci sequence.
    
    Returns:
    list: A list containing the Fibonacci sequence up to n.
    """
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence