def fibonacci(n):
    fib_sequence = []
    if n >= 1:
        fib_sequence.append(0)
    if n >= 2:
        fib_sequence.append(1)
    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)
    return fib_sequence