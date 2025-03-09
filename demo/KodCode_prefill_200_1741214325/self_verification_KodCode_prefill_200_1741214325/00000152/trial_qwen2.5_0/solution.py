def is_even(number):
    """
    Returns True if the number is even, False otherwise.
    Uses bitwise AND operator to determine if the number is even.
    """
    return (number & 1) == 0