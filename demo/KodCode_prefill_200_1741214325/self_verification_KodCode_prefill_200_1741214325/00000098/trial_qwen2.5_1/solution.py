def fibonacci(n):
    """
    Returns the first n terms of the Fibonacci sequence.
    The Fibonacci sequence is a series of numbers where each number is the sum 
    of the two preceding ones, usually starting with 0 and 1.
    
    Parameters:
    n (int): The number of terms in the Fibonacci sequence to generate.
    
    Returns:
    list: A list containing the first n terms of the Fibonacci sequence.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence