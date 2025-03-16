def fibonacci_iterative(n: int) -> int:
    """Returns the n-th Fibonacci number using iteration."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_recursive(n: int, memo={}) -> int:
    """Returns the n-th Fibonacci number using recursion with memoization."""
    if n in memo:
        return memo[n]
    if n <= 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fibonacci_recursive(n - 1, memo) + fibonacci_recursive(n - 2, memo)
    return memo[n]


def fibonacci_binets(n: int) -> int:
    """Returns the n-th Fibonacci number using Binet's formula."""
    import math
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    result = (phi ** n - psi ** n) / sqrt5
    return round(result)


def fibonacci_matrix(n: int) -> int:
    """Returns the n-th Fibonacci number using matrix exponentiation."""
    if n == 0:
        return 0

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
            power //= 2
        return result

    M = [[1, 1], [1, 0]]
    powered_matrix = matrix_power(M, n - 1)
    return powered_matrix[0][0]