def factorial(n):
    """
    Calculates the factorial of a given number n.
    :param n: integer
    :return: factorial of n
    
    Handles edge cases:
    - Factorial of 0 is 1
    - Factorial is not defined for negative numbers, returns None
    """
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result