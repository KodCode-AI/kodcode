def factorial(n: int) -> int:
    """ Calculate the factorial of a number using recursion.
    Args:
        n (int): The input number whose factorial is to be calculated.
    
    Returns:
        int: The factorial of the input number.
    
    Raises:
        ValueError: If the input is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)