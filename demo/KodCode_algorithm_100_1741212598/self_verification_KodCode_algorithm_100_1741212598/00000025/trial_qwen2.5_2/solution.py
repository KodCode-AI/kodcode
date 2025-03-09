def fibonacci_iterative(n):
    """
    Returns the n-th Fibonacci number using iteration.
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_recursive(n, memo={}):
    """
    Returns the n-th Fibonacci number using recursion with memoization.
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_recursive(n - 1, memo) + fibonacci_recursive(n - 2, memo)
    return memo[n]

def fibonacci_binets(n):
    """
    Returns the n-th Fibonacci number using Binet's formula.
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    phi = (1 + 5**0.5) / 2
    return int((phi**n - (-phi)**(-n)) / 5**0.5)

def fibonacci_matrix(n):
    """
    Returns the n-th Fibonacci number using matrix exponentiation.
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    if n == 0:
        return 0
    fib_matrix = [[1, 1], [1, 0]]
    result = matrix_pow(fib_matrix, n - 1)
    return result[0][0]

def matrix_pow(matrix, n):
    """
    Raises a 2x2 matrix to the power of n using exponentiation by squaring.
    """
    result = [[1, 0], [0, 1]]  # Identity matrix
    base = matrix
    while n:
        if n % 2:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        n //= 2
    return result
def matrix_multiply(a, b):
    """
    Multiplies two 2x2 matrices.
    """
    return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]