def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    Args:
    n (int): The input number whose factorial is to be calculated.
    
    Returns:
    int: The factorial of the input number.
    
    Raises:
    ValueError: If the input is a negative integer.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)