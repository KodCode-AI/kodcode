def fibonacci(n):
    if n <= 0:
        return []
    fib_list = []
    a, b = 1, 1
    if n >= 1:
        fib_list.append(a)
    if n >= 2:
        fib_list.append(b)
    for i in range(2, n):
        c = a + b
        fib_list.append(c)
        a, b = b, c
    return fib_list