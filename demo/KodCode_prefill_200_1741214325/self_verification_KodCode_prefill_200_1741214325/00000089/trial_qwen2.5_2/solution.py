def factorial(n):
    """
    Returns the factorial of n. If n is a negative integer, the function returns None.
    For n=0, the function returns 1 as the factorial of 0 is 1.
    """
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result