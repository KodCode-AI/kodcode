def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n, memo={}):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_recursive(n - 1, memo) + fibonacci_recursive(n - 2, memo)
    return memo[n]

def fibonacci_memoization(n):
    return fibonacci_recursive(n)

def fibonacci_binet(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    sqrt_5 = 5 ** 0.5
    phi = (1 + sqrt_5) / 2
    return int(phi ** n / sqrt_5 + 0.5)

def fibonacci_matrix_exponentiation(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    F = [[1, 1], [1, 0]]
    result = [[1, 0], [0, 1]]
    base = 2

    while n > 0:
        if n % 2 == 1:
            result = [[a * b + c * d for a, b in zip(row, col)] for row, col in zip(result, matrix_multiply(result, F))]
        n = n // 2
        F = matrix_multiply(F, F)
    return result[0][0]

def matrix_multiply(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]