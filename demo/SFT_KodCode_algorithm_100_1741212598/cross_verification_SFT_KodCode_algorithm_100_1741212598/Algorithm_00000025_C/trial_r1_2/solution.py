def fibonacci_iterative(n: int) -> int:
    """Returns the n-th Fibonacci number using iteration."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n: int, memo={}) -> int:
    """Returns the n-th Fibonacci number using recursion with memoization."""
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    res = fibonacci_recursive(n - 1, memo) + fibonacci_recursive(n - 2, memo)
    memo[n] = res
    return res

import math

def fibonacci_binets(n: int) -> int:
    """Returns the n-th Fibonacci number using Binet's formula."""
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    return int((phi**n - psi**n) / sqrt5 + 0.5)

def fibonacci_matrix(n: int) -> int:
    """Returns the n-th Fibonacci number using matrix exponentiation."""
    def multiply(m1, m2):
        a = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
        b = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
        c = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
        d = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
        return [[a, b], [c, d]]
    
    def matrix_power(matrix, power):
        result = [[1, 0], [0, 1]]  # Identity matrix
        while power > 0:
            if power % 2 == 1:
                result = multiply(result, matrix)
            matrix = multiply(matrix, matrix)
            power = power // 2
        return result
    
    if n == 0:
        return 0
    matrix = [[1, 1], [1, 0]]
    powered_matrix = matrix_power(matrix, n)
    return powered_matrix[0][1]