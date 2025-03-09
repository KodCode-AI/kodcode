def fibonacci_up_to(n):
    """
    Returns a list of Fibonacci numbers up to a given limit 'n'.
    """
    if n <= 0:
        return []
    fib_list = [0]
    if n == 1:
        return fib_list
    fib_list.append(1)
    while True:
        next_fib = fib_list[-1] + fib_list[-2]
        if next_fib > n:
            break
        fib_list.append(next_fib)
    return fib_list