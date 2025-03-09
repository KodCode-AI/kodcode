def max_without_conditions(a, b):
    """
    Returns the maximum of two numbers without using if-else statements or comparison operators.
    """
    return a + ((a - b) >> 31) & b + ((b - a) >> 31)