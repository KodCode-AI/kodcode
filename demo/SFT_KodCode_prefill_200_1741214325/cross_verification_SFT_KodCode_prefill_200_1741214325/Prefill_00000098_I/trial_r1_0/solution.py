def fibonacci(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_term = fib_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(next_term)
        return fib_sequence