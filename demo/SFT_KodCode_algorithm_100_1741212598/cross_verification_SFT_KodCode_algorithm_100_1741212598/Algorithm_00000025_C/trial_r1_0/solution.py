import math

def fibonacci_iterative(n: int) -> int:
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n: int, memo={}) -> int:
    if n in memo:
        return memo[n]
    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_recursive(n - 1, memo) + fibonacci_recursive(n - 2, memo)
    memo[n] = result
    return result

def fibonacci_binets(n: int) -> int:
    if n == 0:
        return 0
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    return int((phi ** n - psi ** n) / sqrt5 + 0.5)

def fibonacci_matrix(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    def multiply(m1, m2):
        a = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
        b = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
        c = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
        d = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
        return [[a, b], [c, d]]
    
    def power(mat, exponent):
        result = [[1, 0], [0, 1]]  # Identity matrix
        while exponent > 0:
            if exponent % 2 == 1:
                result = multiply(result, mat)
            mat = multiply(mat, mat)
            exponent = exponent // 2
        return result
    
    mat = [[1, 1], [1, 0]]
    mat_power = power(mat, n - 1)
    return mat_power[0][0]