def is_fibonacci(n):
    if n == 0 or n == 1:
        return True
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
        if a == n:
            return True
    return False