def fibonacci(n):
    if n <= 0:
        return []
    fibs = []
    a, b = 1, 1
    for _ in range(n):
        fibs.append(a)
        a, b = b, a + b
    return fibs