def is_power_of_two(n):
    """
    Returns True if n is a power of two, otherwise returns False.
    """
    if n <= 0:
        return False
    return (n & (n - 1)) == 0