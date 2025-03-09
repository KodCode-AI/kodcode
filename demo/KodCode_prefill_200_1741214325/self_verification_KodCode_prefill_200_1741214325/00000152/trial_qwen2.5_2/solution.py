def is_even(number):
    """
    Returns True if the number is even, False otherwise, using bitwise operations only.
    """
    return (number & 1) == 0