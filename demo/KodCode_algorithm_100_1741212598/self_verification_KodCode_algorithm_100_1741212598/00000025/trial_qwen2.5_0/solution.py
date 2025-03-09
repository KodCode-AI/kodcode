def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("Input should be non-negative")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_memoization(n, memo={}):
    if n < 0:
        raise ValueError("Input should be non-negative")
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

def fibonacci_binet(n):
    if n < 0:
        raise ValueError("Input should be non-negative")
    
    sqrt_5 = 5 ** 0.5
    phi = (1 + sqrt_5) / 2
    return round((phi ** n - (-phi) ** (-n)) / sqrt_5)

def fibonacci_matrix(n):
    if n < 0:
        raise ValueError("Input should be non-negative")
    
    matrix = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    def multiply(F, M):
        x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
        y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
        z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
        w = F[1][0] * M[0][1] + F[1][1] * M[1][1]
        
        F[0][0], F[0][1], F[1][0], F[1][1] = x, y, z, w
    
    def power(F, n):
        if n == 0 or n == 1:
            return
        M = [[1, 1], [1, 0]]
        power(F, n // 2)
        multiply(F, F)
        
        if n % 2 != 0:
            multiply(F, M)
    
    power(matrix, n - 1)
    return matrix[0][0]