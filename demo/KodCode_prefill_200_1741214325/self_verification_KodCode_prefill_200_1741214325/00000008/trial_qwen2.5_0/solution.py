def max_without_if_else(a, b):
    """
    Returns the maximum of two numbers without using if-else statements or comparison operators.
    """
    return a + ((b - a) >> 31) & b