def factorial(n):
    """
    Calculate the factorial of a given number.
    
    Args:
    n (int): The input number for which the factorial is to be calculated.
    
    Returns:
    int: The factorial of the input number. Returns 1 for n=0 and raises ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result