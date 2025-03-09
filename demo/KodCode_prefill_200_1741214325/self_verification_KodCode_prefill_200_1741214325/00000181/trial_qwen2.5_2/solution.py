def fibonacci_up_to_n(n):
    """
    Returns a list of Fibonacci numbers up to n.
    
    Parameters:
    n (int): The upper limit for generating Fibonacci numbers.
    
    Returns:
    list: A list of Fibonacci numbers.
    """
    if n < 1:
        return []
    fibonacci_list = [0, 1]
    while True:
        next_fib = fibonacci_list[-1] + fibonacci_list[-2]
        if next_fib > n:
            break
        fibonacci_list.append(next_fib)
    return fibonacci_list